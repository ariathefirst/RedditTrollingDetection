import praw
import csv
import json
import time
import collections
from csv import DictReader
from googleapiclient import discovery
import sys

with open('ID.txt', encoding = 'utf-8') as input_file:
    ID = [row["ID"] for row in DictReader(input_file)]

reddit = praw.Reddit(user_agent= 'comment scrape',
    client_id='x4IhHsDXOvCJOA',
    client_secret="sAD1CgtndyINl-lpd06Q2xw4ZbI",
    username='Rei_rest',
    password='mitsudome1')

for i in ID:
    submissions = [reddit.submission(id =i)]
    for instance in submissions:
        instance.comments.replace_more(limit=0)
        comments = instance.comments.list()
        if comments:
            print("It is a submission link")
        else:
            print("X")


#to check 1 ID for submission

##submissions = [reddit.submission(id = "8.72E+14")]
##for instance in submissions:
##    instance.comments.replace_more(limit=0)
##    comments = instance.comments.list()
##    if comments:
##        print("It is a submission link")
##    else:
##        print("Nah")

#to check 1 ID for comment

##comments = reddit.comment(id = "8.72E+14")
##print(comments.body)
##
print("done")

