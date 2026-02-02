# %%

import pandas as pd

import sys, argparse

# %%

def num2word(s: str = 'Example 1234'):

    return 'Hello World'

s = 'Example 1234'

# %%

def main():

    # start arg parser
    parser = argparse.ArgumentParser(
                        prog='num2word.py',
                        description='A function that finds a single number in a string converts the given number into words. For example, given the number “1234” as input, return the output “one thousand, two hundred and thirty-four".')


    # optional, otherwise always file takes presedance
    parser.add_argument(
        'sentence',
        type=str,
        nargs='?',
        help='Optional string to parse via stdin.')

    parser.add_argument(
        '--file',
        type=str,
        help='Text file with string data. Multi line file will be read as single piece of text.')
    
    args = parser.parse_args()

    if args.file:
        # read from file
        print(f"---> reading from file: {args.file}")
    elif args.sentence:
        # else use command line input
        print(f"---> sentence: {args.sentence}")
    else:
        parser.print_help()

# %%

if __name__ == '__main__':

    main()
