import numpy as np, sympy #np arrays are just nice in general
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
    ans1 = 0
    lines = open(filename).read().splitlines()
    lines = list(map(int,lines))
    for line in range(len(lines)-1):
        if lines[line] < lines[line+1]:
            ans1 += 1
    
    ans2 = 0
    for a in range(3,len(lines)):
        if sum(lines[a-3:a]) < sum(lines[a-2:a+1]):
            ans2 += 1
    print(ans1)
    print(ans2)

run("example.txt")
print()
run("day1.txt")
