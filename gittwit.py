#!/usr/bin/env python

import oauth2
import json
import csv

API_KEY = your key
API_SECRET = your key
TOKEN_KEY = your key
TOKEN_SECRET = your key

def  oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
	consumer =oauth2.Consumer(key=API_KEY, secret=API_SECRET)
	token = oauth2.Token(key=key, secret=secret)
	client = oauth2.Client(consumer,token)
	resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
	return content

url='https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=sammmy99&count=15'
data = oauth_req(url, TOKEN_KEY, TOKEN_SECRET)

data=json.loads(data)

	

csv_out = open('tweets_out.csv', 'w') #opens csv file
writer = csv.writer(csv_out) #create the csv writer object
fields = ['created_at', 'text', 'screen_name', 'followers', 'friends', 'rt', 'fav'] #field names
writer.writerow(fields) #writes field

for line in data:

    #writes a row and gets the fields from the json object
    #screen_name and followers/friends are found on the second level hence two get methods
    writer.writerow([line.get('created_at'),
                     line.get('text').encode('unicode_escape'), #unicode escape to fix emoji issue
                     line.get('user').get('screen_name'),
                     line.get('user').get('followers_count'),
                     line.get('user').get('friends_count'),
                     line.get('retweet_count'),
                     line.get('favorite_count')])

csv_out.close()