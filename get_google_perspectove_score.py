import praw
import datetime
import csv
import json
import pandas as pd
import googleapiclient
from googleapiclient import discovery
import sys

# sound alarm if program halts
import os

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

def getPerspective(res_file, file):
	i = 0
	try:
		with open(res_file, "w+") as w:
			writer = csv.writer(w, delimiter = ",")
			with open(file, 'rU') as f:
				comment_res = csv.reader(f, delimiter = ",")
				for item in comment_res: # for each row
					print(i)
					if i == 0:
						item.append("perspective_score") # adds pscore attribute
						item.append("p_perspective_score")
					elif i > 4035:
						pscore = runPerspective(item[1]) # gets pscore of comment
						p_pscore = runPerspective(item[11]) # gets parent pscore of comment
						item.append(pscore) # appends pscore to end of row
						item.append(p_pscore) 
						writer.writerow(item) # write cur row to output file res_file
					i = i + 1
	except:
		duration = 1  # second
		freq = 440  # Hz
		os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
		os.system('say "your program stopped unexpectedly"')
	print("done")
	os.system('say "your program has finished"')

def main(): # change this to a loop to call all files within a bigQueryData dir
	# getPerspective("pineapplecharmPscore.csv", "bigQueryData/pineapplecharm.csv")
	# getPerspective("sosorrynonamePscore.csv", "bigQueryData/sosorrynoname.csv")
	# getPerspective("parent_id=t3_20myzoPscore.csv", "bigQueryData/parent_id=t3_20myzo.csv")
	getPerspective("all_result4.csv", "bigQueryData/all_result1.csv")

if __name__== "__main__":
	main()



