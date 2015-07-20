# -*- coding: utf-8 -*-
import time
import praw
import os
import traceback
import requests
print "      __     __ _                            _                        _     _                "
print " the / /    / /| |                          (_)                      | |   (_)               "
print "    / / __ / /_| | ___   __ _  ___  ___ ___  _ _ __     __ _ _ __ ___| |__  ___   _____ _ __ "
print "   / / '__/ / _` |/   \ / _` |/ _ \/ __/ _ \| | '_ \   / _` | '__/ __| '_ \| \ \ / / _ \ '__|"
print "  / /| | / / (_| | (_) | (_| |  __/ (_| (_) | | | | | | (_| | | | (__| | | | |\ V /  __/ |  "
print " /_/ |_|/_/ \__,_|\___/ \__, |\___|\___\___/|_|_| |_|  \__,_|_|  \___|_| |_|_| \_/ \___|_| project"
print "                         __/ |   "
print "                        |___/           code-name: chugger  "
print "Code written by: /u/peoplma and /u/healdb"
print "Sillines added by: /u/joshtheimpaler"
print "Wow by: /r/dogecoin"

print("Searching for posts... it may not look like it, but I AM actually doing something.")

b = "timestamp:"
d = ".."

#Config Details-
r = praw.Reddit('searchandarchive by ')
folderName="subArchive"
startStamp=1386641400
endStamp=1437350401
#Seconds
step=30
subName = "dogecoin"

if not os.path.exists(folderName):
    os.makedirs(folderName)
    
def getNew(subName,folderName):
    subreddit_comment = r.get_comments(subName, limit=1000)
    subreddit_posts = r.get_submissions(subName, limit=1000)
    for comment in subreddit_comment:
        print comment
        url= comment.permalink
        data= {'user-agent':'archive by /u/healdb'}
        #manually grabbing this file is much faster than loading the individual json files of every single comment, as this json provides all of it
        if comment.id not in already_done:
            response = requests.get(url+'.json',headers=data)
            #Create a folder called dogecoinArchive before running the script
            filename=folderName+"/"+comment.name
            obj=open(filename, 'w')
            obj.write(response.text)
            obj.close()
            #print post_json
            already_done.add(comment.id)
        else:
            continue
    for post in subreddit_posts:
        print post
        url1= post.permalink
        #pprint(vars(post))
        data= {'user-agent':'archive by /u/healdb'}
        #manually grabbing this file is much faster than loading the individual json files of every single comment, as this json provides all of it
        if submission.id not in already_done:
            response = requests.get(url1+'.json',headers=data)
            #Create a folder called dogecoinArchive before running the script
            filename=folderName+"/"+post.name
            obj=open(filename, 'w')
            obj.write(response.text)
            obj.close()
            #print post_json
            already_done.add(submission.id)
        else:
            continue
def main(startStamp,endStamp,step,folderName,subName):
    try:
        startStamp =open(folderName+"/lastTimestamp.txt").read()
        print("Got last timestamp from file: " + startStamp)
        startStamp=int(startStamp)
    except: 
        pass
    for currentStamp in range(startStamp,endStamp,step):
        f = str(currentStamp)
        g = str(currentStamp+30)
        search_results = r.search(b+f+d+g, subreddit=subName, syntax='cloudsearch')
        print(str(b+f+d+g))
        for post in search_results:
            print("---I found a post! It\'s called:" + str(post))
            url= (post.permalink).replace('?ref=search_posts','')
            #pprint(vars(post))
            data= {'user-agent':'archive by /u/healdb'}
            #manually grabbing this file is much faster than loading the individual json files of every single comment, as this json provides all of it
            response = requests.get(url+'.json',headers=data)
            #Create a folder called dogecoinArchive before running the script
            filename=folderName+"/"+post.name+'.json'
            obj=open(filename, 'w')
            obj.write(response.text)
            obj.close()
            #print post_json
            print("I saved the post and named it " + str(post.name) + " .---")
        obj=open(folderName+"/lastTimestamp.txt", 'w')
        obj.write(str(currentStamp))
        obj.close()
    print('Welp, all done here! Stopped at timestamp '+ str(currentStamp))

while True:
    try:
        main(startStamp,endStamp,step,folderName,subName)
        print("Succesfully got all posts within parameters. Now archiving all new posts and comments.")
        while True:
            getNew(subName,folderName)
    except:
        print("Error in the program! The error was as follows: ")
        error = traceback.format_exc()
        time.sleep(5)
        print(error)
        time.sleep(5)
        print("Resuming in 5 seconds...")
        time.sleep(5)
