import numpy as np #np arrays are just nice in general
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
import collections #defaultdicts, maybe counters
import functools #use @functools.lru_cache(None) above a function to keep track of all inputs and speed it up
import string #ascii_uppercase, ascii_lowercase, etc..
import itertools #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
from copy import deepcopy #deepcopy() let's use copy a list without reference areas
#Sets are POG {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))

def run(filename):
    print("Running",filename+"...")

    fish = list(map(int,open(filename).read().split(',')))
    fish = {i:sum(1 if j==i else 0 for j in fish) for i in range(9)}
    for day in range(256):
        new = {i:fish[i+1] for i in range(8)}
        new[6] += fish[0]
        new[8] = fish[0]
        fish = new
        if day == 79: print(sum(fish.values()))
    print(sum(fish.values()))
        


run("example.txt")
print()
run("day6.txt")