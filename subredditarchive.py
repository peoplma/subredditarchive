import time
import praw
import random
import re
import urllib2
import sys
import traceback
from pprint import pprint

subName = 'dogecoin'
r = praw.Reddit('searchandarchive')
a = 'timestamp:1386460800..1386547200'
b = 'timestamp:'
c = str(1391212800)
d = '..'
e = str(1393632000)
r.config.store_json_result = True
def main():
	def my_range(start, end, step):
		while start <= end:
			yield start
			start += step

	for c in my_range(1391212800, 1393632000, 60):
		f = str(c)
		g = str(c+60)
		print c
		search_results = r.search(b+f+d+g, subreddit=subName, sort='new', syntax='cloudsearch')
		if c >= 1393632000:
			print 'DONE!!!!!!!!'
		else:
			for post in search_results:
				print post
				#pprint(vars(post))
				post_json = post.json_dict
				post_jsonstr = str(post_json)
				open('rdogecoinarchive.txt', 'ab+')
				obj = open('rdogecoinarchive.txt', 'ab+')
				obj.write(post_jsonstr)
				obj.close()
				#print post_json
				post.replace_more_comments(limit=10000, threshold=-10000)
				flat_comments = praw.helpers.flatten_tree(post.comments)
				for comment in flat_comments:
					comment_json = comment.json_dict
					#print comment_json
					comment_jsonstr = str(comment_json)
					open('rdogecoinarchive.txt', 'ab+')
					obj = open('rdogecoinarchive.txt', 'ab+')
					obj.write(comment_jsonstr)
					obj.close()
	
def secondary():
	try:
		while True:
			main()
	except:
		traceback.print_exc()
		print('Resuming in 2min...')
		time.sleep(120)
while True:
	secondary()
	
