import logging
import argparse
from dotenv import load_dotenv
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

load_dotenv()
SECRET_ENV=os.getenv("SECRET_ENV")

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
    args = arg_parse()
    name = args.name
    age = args.age

    utility = Utility(name=name, age=age)
    utility.hello()

if __name__ == '__main__':
    main()

