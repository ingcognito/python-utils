import logging
import csv
import os
import argparse
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

def arg_parse():
    parser = argparse.ArgumentParser(description='Parsin some args')
    parser.add_argument('--name', required=True, type=str,
                        help='name of person')
    parser.add_argument('--age', required=True, type=str,
                        help='age of person')
    args = parser.parse_args()
    return args


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
        with open(f'{screen_name}_tweets.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["id","created_at","text"])
            writer.writerows(outtweets)

        pass
        
    def run(self):
        print(self.twitter.statuses.home_timeline())

def main():
    # args = arg_parse()
    # name = args.name
    # age = args.age
    util = TwitterUtility()
    util.get_all_user_tweets("ingcognito92")


if __name__ == '__main__':
    main()
