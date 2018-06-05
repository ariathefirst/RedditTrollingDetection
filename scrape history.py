import praw
import csv
import json
import time
import collections
from csv import DictReader
import sys    

names = collections.Counter()
omit = ['AutoModerator', '']
#counts number of authors, excluding AutoModerator and blank
with open('redditposttop.csv', encoding = 'utf-8') as input_file:
    for row in csv.reader(input_file):
        if row[0] in omit:
            names[row[0]] = 0
        else:
            names[row[0]] += 1
            
#pulls the most x common names and how many times they appear
list1 = names.most_common(20)

#just pulls the names
list2 = []
for i in range(0,20):
    list2.append(list1[i][0])

with open('redditposttop.csv', encoding = 'utf-8') as input_file:
    sub_link = [row["Submission Link"] for row in DictReader(input_file)]


source = 'redditorhistory.csv'

reddit = praw.Reddit(user_agent= '',
    client_id='',
    client_secret="",
    username='',
    password='')

def getRecent1 (filename):
    #csv file setup
    with open(filename, 'w', newline='', encoding = 'utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["Author", "Comment Id", "Parent Id", "Timestamp", "Comment Body", "Parent Comment Body"])
        for author1 in list2:
            redditor1 = reddit.redditor(author1) #loop each author in list2 to get comments etc. 
            for comment in redditor1.comments.new(limit = None):
                author = comment.author #name of author
                id = comment.fullname #comment ID
                parentId = comment.parent().fullname #parent ID, ie. t3_8lmf26
                timestamp = comment.created_utc
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp)) #change to local time
                body = comment.body #actual comment
                parent = comment.parent()
                #GP_score = runPerspective(body)
                if comment.is_root == True:
                    parent1 = "It is the first comment on the post"
                    #GP_score_p = "No Score"
                else:
                    parent1 = parent.body #actual parent comment
                    #GP_score_p = runPerspective(parent.body)
                #write to csv file with header
                writer.writerow([author, id, parentId, timestamp, body, parent1])

getRecent1(source)
print(list1) #to print list of most commented
print("done")
