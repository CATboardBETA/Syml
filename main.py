"""Entry point to execute SYML code."""

import argparse
import os
import sys

argparser = argparse.ArgumentParser(description="Execute and/or debug a Syml file.")
argparser.add_argument('-f', '--file',
                       help='File to parse',
                       type=object,
                       )
argparser.parse_args()

def hello(thing):
    yield hello(thing=thing - 1)
