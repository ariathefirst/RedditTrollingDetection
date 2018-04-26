import requests
import urllib
import json
import csv

# Can get a max of 500 comments per call
subreddit_url = 'https://api.pushshift.io/reddit/search/comment/?subreddit=politics&size=500'

r = requests.get(test_url)

page_json = r.json()

# Note 1: All the information we want is in page_json['data']
# Note 2: page_json['data'] is a list of dicts
# print(page_json['data'])

count = 1

with open('dataset.csv', 'w', newline='') as csvfile:
	csv_writer = csv.writer(csvfile, delimiter=',')
	csv_writer.writerow(["#", "Subreddit", "Submission Link", "Author", "Comment Body", "Timestamp", "Parent Comment", "Comment Score"])
	while(count < 500):
		
		print('-------------------')
		print(count)
		# print(page_json['data'][count]['author'])
		# print(page_json['data'][count]['body'])

		# Get parent comment
		try:
			parent_id = page_json['data'][count]['parent_id']
			parent_url = 'https://api.pushshift.io/reddit/search/comment/?id=' + parent_id
			p = requests.get(parent_url)
			parent_json = p.json()

		except:
			parent_id = "No Parent"

		# Write to CSV
		row = [count, page_json['data'][count]['subreddit'], page_json['data'][count]['link_id'], page_json['data'][count]['author'], page_json['data'][count]['body'], page_json['data'][count]['created_utc'], page_json['data'][count]['parent_id'], page_json['data'][count]['score']]
		csv_writer.writerow(row)
		count += 1

print("Done")