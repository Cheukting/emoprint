import builtins
from .pick_emoji import pick_emoji
import sys

def nlp_print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    pricked = pick_emoji(str(*objects))
    builtins.print(*objects, pricked)
