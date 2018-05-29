import praw
import datetime
import csv
import json
import pandas as pd
import googleapiclient
from googleapiclient import discovery
import sys

def runPerspective(str):
	# print("what?\n")
	# print(str)
	# print("printed str")
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

i = 0
pScore = "pineapplecharmPscore.csv"
with open(pScore, "w+") as w:
	writer = csv.writer(w, delimiter = ",")
	with open("pineapplecharm.csv", 'rU') as f:
		comment_res = csv.reader(f, delimiter = ",")
		for item in comment_res: # for each line
			pscore = runPerspective(item[0])
			# if i == 5:
			# 	break	
			if i == 0:
				item.append("pscore") 
				print(item[7])
			else:
				item.append(pscore)
				print(item[7])
			i = i + 1
			print("item is")
			print(item)
			writer.writerow(item)
print("done")


