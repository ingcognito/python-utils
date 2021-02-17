import logging
import csv
import os
import json
import sys
import tweepy
from dotenv import load_dotenv
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

load_dotenv()
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token_key")
access_token_secret = os.getenv("access_token_secret")
twitter_username = ""

class TwitterUtility:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret) 
        self.api = tweepy.API(self.auth)

    def get_all_user_tweets(self, screen_name):
        api = self.api 

        #initialize a list to hold all the tweepy Tweets
        alltweets = []

        #make initial request for most recent tweets (200 is the maximum allowed count)
        new_tweets = api.user_timeline(screen_name = screen_name,count=200)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        #keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
            print(f"getting tweets before {oldest}")

            #all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

            #save most recent tweets
            alltweets.extend(new_tweets)

            #update the id of the oldest tweet less one
            oldest = alltweets[-1].id - 1

            print(f"...{len(alltweets)} tweets downloaded so far")

        #transform the tweepy tweets into a 2D array that will populate the csv
        outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]

        #write the csv
        with open(f'{twitter_username}_tweets.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["id","created_at","text"])
            writer.writerows(outtweets)

        pass

    def batch_delete(self):
        api = self.api 
        with open(f'{twitter_username}_tweets.csv', 'r') as f:
            tweets = csv.reader(f)
            for row in tweets:
                print(row[0])
                status = row[0]
                try:
                    api.destroy_status(status)
                    print(f"Deleted: {status}")
                except:
                    print(f"Failed to delete: {status}")
        
def main():
    util = TwitterUtility()
    util.get_all_user_tweets(self)
    util.batch_delete()


if __name__ == '__main__':
    main()
