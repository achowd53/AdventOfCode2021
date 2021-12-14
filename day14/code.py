import numpy as np #np arrays are just nice in general
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
import collections #defaultdicts, maybe counters
import functools #use @functools.lru_cache(None) above a function to keep track of all inputs and speed it up
import string #ascii_uppercase, ascii_lowercase, etc..
import itertools #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
import networkx #Networkx for graph problems like connected components
from copy import deepcopy #deepcopy() let's use copy a list without reference areas
#Sets are POG {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))

def run(filename):
    print("Running",filename+"...")

    lines = open(filename).read().split('\n\n')
    map = {i:j for i,j in [line.split(' -> ') for line in lines[1].split('\n')]}
    amount_pairs = collections.defaultdict(int)
    amount_singles = collections.defaultdict(int)
    for i in range(len(lines[0])-1):
        amount_pairs[lines[0][i]+lines[0][i+1]] += 1
        amount_singles[lines[0][i]] += 1
    amount_singles[lines[0][-1]] += 1
    for i in range(40):
        new_amount_pairs = collections.defaultdict(int)
        for j in amount_pairs :
            amount_singles[map[j]] += amount_pairs[j]
            new_amount_pairs[j[0]+map[j]] += amount_pairs[j]
            new_amount_pairs[map[j]+j[1]] += amount_pairs[j]
        amount_pairs = new_amount_pairs
        if i in [9,39]: print(max(amount_singles.values())-min(amount_singles.values()))
   


run("example.txt")
print()
run("day14.txt")