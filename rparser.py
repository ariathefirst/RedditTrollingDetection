import praw
import datetime
import csv
import json
import googleapiclient
from googleapiclient import discovery
import sys

def runPerspective(str):
	API_KEY='AIzaSyAlCwhKJ0C8n4eFM-ioPC5-MCFYy4P-TT8'

	# Generates API client object dynamically based on service name and version.
	service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)

	analyze_request = {
		'comment': { 'text': str },
		'requestedAttributes': {'TOXICITY': {}}
	}
	try:
		response = service.comments().analyze(body=analyze_request).execute()
		json.dumps(response)
		return response["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
		# print response.attributeScores.TOXICITY.summaryScore.value
	except googleapiclient.errors.HttpError as e:
		return "Error!"	

	

reddit = praw.Reddit(client_id='OlM6d2hKSrhbkw',
                     client_secret='w3kllzs-03WScaa9DFMHvRdTnQg',
                     password='WebW0rld',
                     user_agent='script by /u/sravyadivakarla123',
                     username='sravyadivakarla123')

csvFile = str(sys.argv[1]) # python rparser.py "csvFileName"
print (csvFile)

all_Users = []

with open(csvFile, 'rU') as f:
    reader = csv.reader(f, delimiter=',')

    # Each item is a list containing all items in the row, aka every comment and associated features
    for item in reader:
    	all_Users.append(item[2]) # adding every user name
    	# print("cur user is ",item[2])



fileName = "TEST.csv" 

# for user in all_Users:
# 	with open(fileName,'a') as f1:
# 		writer = csv.writer(f1, delimiter=',')
# 		# writer.writerow(["User","#","Comment","Timestamp(PT)", "Comment Score", "Number of Comments in Post", "Perpective Score"])
# 		index = 0
# 		try:
# 			for comment in reddit.redditor(user).comments.new(limit=10000): # calls praw redditor api
# 			# replaced by iterating through every comment 

# 				index += 1
# 				perspectiveScore = runPerspective(comment.body)
# 				row = [user,index,comment.body.encode('utf8'),datetime.datetime.fromtimestamp(int(comment.created_utc)).strftime('%Y-%m-%d %H:%M:%S').encode('utf8'), comment.score, comment.num_comments, perspectiveScore]
# 				writer.writerow(row)
# 			print (user)
# 		except:
# 			print ("ERROR " + user)

for user in all_Users:
	with open(fileName,'a') as f1:
		writer = csv.writer(f1, delimiter=',')
		writer.writerow(["User","#","Comment","Timestamp(PT)", "Comment Score", "Number of Comments in Post", "Perpective Score"])
		index = 0
		try:
			for comment in reddit.redditor(user).comments.new(limit=10000):
				print(comment)
				index += 1
				perspectiveScore = runPerspective(comment.body)
				row = [user,index,comment.body.encode('utf8'),datetime.datetime.fromtimestamp(int(comment.created_utc)).strftime('%Y-%m-%d %H:%M:%S').encode('utf8'), comment.score, comment.num_comments, perspectiveScore]
				writer.writerow(row)
			print (user)
		except:
			print ("ERROR " + user)

print("done")