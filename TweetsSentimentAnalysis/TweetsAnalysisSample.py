import csv
import time
from dotenv import load_dotenv
load_dotenv('.env')
import os
import tweepy
from  textblob import TextBlob 


consumer_key=os.getenv("CONSUMER_KEY")
consumer_secret=os.getenv("CONSUMER_SECRET")
access_token =os.getenv("ACCESS_TOKEN")
access_secret=os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth)

tweet_search = api.search_tweets('Aryan Khan')

pos='positive'
neg='negative'
positive_count=0
negative_count=0

header = ["pos","neg","positive_count","negative_count"]
try:
   with open('tweets.csv', 'w') as csv_file:
         csv_writer = csv.DictWriter(csv_file, fieldnames=header)
         csv_writer.writeheader()

   while True:
   # printing line by line
      with open('tweets.csv', 'a') as csv_file:
          
         for tweet in tweet_search:
            print(tweet.text)
            analysis=TextBlob(tweet.text) 
            print(analysis.sentiment)
           
            if analysis.sentiment.polarity > 0:
               print("positive")
               positive_count = positive_count + 1
            elif analysis.sentiment[0]<0:
               print("Negative")
               negative_count = negative_count + 1
            else :
               print("Neutral")

            csv_writer = csv.DictWriter(csv_file, fieldnames=header)
            details = {
                     "pos": pos,
                     "neg": neg,
                     "positive_count":positive_count,
                     "negative_count":negative_count
                     }
            csv_writer.writerow(details)
            time.sleep(1) 
            print(positive_count,negative_count)

except Exception as e:
   print(e)