import logging
import argparse
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def arg_parse():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    
    args = parser.parse_args()
    print(args.accumulate(args.integers))


def base():
    logging.warning('is when this event was logged.')

if __name__ == '__main__':
    base()

