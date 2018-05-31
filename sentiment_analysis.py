#By Haoran Zhang
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions, EmotionOptions, SentimentOptions
import pandas as pd

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='{username}',
  password='{password}',
  version='2018-03-16')

data = pd.read_csv("all_result.csv")
sadness=[]
joy=[]
fear=[]
disgust=[]
anger=[]
sentiment_score=[]
p_sadness=[]
p_joy=[]
p_fear=[]
p_disgust=[]
p_anger=[]
p_sentiment_score=[]
j = 0
for i in data['body']:
  print("Analyzing original post:",j)
  j=j + 1
  try:
    response = natural_language_understanding.analyze(
        text=i,
        features=Features(
          emotion=EmotionOptions(
            document=True),
        sentiment=SentimentOptions(
            document=True)))
    sadness.append(response['emotion']['document']['emotion']['sadness'])
    joy.append(response['emotion']['document']['emotion']['joy'])
    fear.append(response['emotion']['document']['emotion']['fear'])
    disgust.append(response['emotion']['document']['emotion']['disgust'])
    anger.append(response['emotion']['document']['emotion']['anger'])
    sentiment_score.append(response['sentiment']['document']['score'])
  except:
    sadness.append('NA')
    joy.append('NA')
    fear.append('NA')
    disgust.append('NA')
    anger.append('NA')
    sentiment_score.append('NA')
data['sadness']=sadness
data['joy']=joy
data['fear']=fear
data['disgust']=disgust
data['anger']=anger
data['sentiment_score']=sentiment_score

j = 0
for i in data['p_body']:
  print("Analyzing parent posts:",j)
  j=j + 1
  try:
    response = natural_language_understanding.analyze(
        text=i,
        features=Features(
          emotion=EmotionOptions(
            document=True),
        sentiment=SentimentOptions(
            document=True)))
    p_sadness.append(response['emotion']['document']['emotion']['sadness'])
    p_joy.append(response['emotion']['document']['emotion']['joy'])
    p_fear.append(response['emotion']['document']['emotion']['fear'])
    p_disgust.append(response['emotion']['document']['emotion']['disgust'])
    p_anger.append(response['emotion']['document']['emotion']['anger'])
    p_sentiment_score.append(response['sentiment']['document']['score'])
  except:
    p_sadness.append('NA')
    p_joy.append('NA')
    p_fear.append('NA')
    p_disgust.append('NA')
    p_anger.append('NA')
    p_sentiment_score.append('NA')
data['p_sadness']=p_sadness
data['p_joy']=p_joy
data['p_fear']=p_fear
data['p_disgust']=p_disgust
data['p_anger']=p_anger
data['p_sentiment_score']=p_sentiment_score

data.to_csv('all_result1.csv')