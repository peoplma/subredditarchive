# subredditarchive
saves all .json data from posts and comments in a subreddit

#Dependencies
Reddit's PRAW: https://praw.readthedocs.org/en/v3.1.0/

#What does it do?

It searches from a given timestamp in reddit and downloads the .json data from the post and the top 200 comments in it.

#Why do I need this?

If you'd like your favorite subreddit's data stored somewhere else other than on reddit.com's servers, then this bot is for you.

#K, so how to use the script?

The script will ask you to input the subereddit you want to archive, the timeframe you want to download, and the interval you want to do API calls in.  For example, if you choose July 1, 2013 to July 2, 2013 and a 60 second interval, it will pull all posts for that day, searching every minute of the day for posts.  If there are more than 25 posts in the time interval chosen, it will miss some, so make sure you are conservative when choosing an interval.

#Customize

The new version of the script is customized by user inputs at start up.  Thanks @healdb

