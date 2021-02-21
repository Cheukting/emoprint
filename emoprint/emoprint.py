import builtins
import random
import sys
from os.path import abspath, dirname

EMOS = open(dirname(abspath(__file__))+"/emolist.txt", "r").read()

def print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    builtins.print(*objects, random.choice(EMOS))