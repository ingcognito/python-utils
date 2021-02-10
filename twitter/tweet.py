import logging
import os
import argparse
import json
import sys
from twitter import *
from dotenv import load_dotenv
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

load_dotenv()
CONSUMER_KEY = os.getenv("consumer_key")
CONSUMER_SECRET = os.getenv("consumer_secret")
ACCESS_TOKEN_KEY = os.getenv("access_token_key")
ACCESS_TOKEN_SECRET = os.getenv("access_token_secret")

def arg_parse():
    parser = argparse.ArgumentParser(description='Parsin some args')
    parser.add_argument('--name', required=True, type=str,
                        help='name of person')
    parser.add_argument('--age', required=True, type=str,
                        help='age of person')
    args = parser.parse_args()
    return args


class Utility:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def hello(self):
        name = self.name
        age = self.age
        print(f" Hello my name is {name}, I am {age} years old")

def main():
    # args = arg_parse()
    # name = args.name
    # age = args.age

    # utility = Utility(name=name, age=age)
    # utility.hello()
    t = Twitter(auth=OAuth(consumer_key=CONSUMER_KEY,consumer_secret=CONSUMER_SECRET, token=ACCESS_TOKEN_KEY, token_secret=ACCESS_TOKEN_SECRET))
    print(t.statuses.home_timeline())


if __name__ == '__main__':
    main()
