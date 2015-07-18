# subredditarchive
saves all .json data from posts and comments in a subreddit

#What does it do?

It searches from a given timestamp in reddit and downloads the .json data from the post and all comments.

#Why do I need this?

If you'd like your favorite subreddit's data stored somewhere else other than on reddit.com's servers, then this bot is for you.

#K, so how to use the script?

The current script that's uploaded searches /r/dogecoin for all posts and comments between the time period from 1391212800 to 1393632000 (Feb 1, 2013 to March 1, 2013).

#Customize

The current script downloads .json data from /r/dogecoin, and pastes it in a .txt file called rdogecoinarchive.txt.  You can edit this file name.  This script searches from the time intervals defined by `for c in my_range(1391212800, 1393632000, 60):`.  You can change these time intervals to suit your subreddit by converting at http://www.onlineconversion.com/unix_time.htm.  You will retrieve up to 25 posts and their comments every minute with this script.  You can increase or decrease the number entries received with for c in my_range(1391212800, 1393632000, 60):

