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

    lines = open(filename).read().splitlines()
    count_p1 = collections.defaultdict(int)
    count_p2 = collections.defaultdict(int)
    for line in lines:
        line = re.search('(.*),(.*) -> (.*),(.*)', line)
        a,b,c,d = int(line.group(1)),int(line.group(2)),int(line.group(3)),int(line.group(4))
        dx = 1 if a < c else (0 if a==c else -1)
        dy = 1 if b < d else (0 if b==d else -1)
        while (a,b) != (c,d):
            if abs(dx)^abs(dy): count_p1[(a,b)] += 1
            count_p2[(a,b)] += 1
            a, b = a+dx, b+dy 
        if abs(dx)^abs(dy): count_p1[(c,d)] += 1
        count_p2[(c,d)] += 1
    print(sum(1 if i > 1 else 0 for i in count_p1.values()))
    print(sum(1 if i > 1 else 0 for i in count_p2.values()))
    
run("example.txt")
print()
run("day5.txt")