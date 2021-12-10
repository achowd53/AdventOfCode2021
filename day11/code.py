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

    lines = open(filename).read().splitlines()
    points1 = {')':3,']':57,'}':1197,'>':25137}
    points2 = {'(':1,'[':2,'{':3,'<':4}
    ans1 = 0
    ans2 = []
    for line in lines:
        stack = []
        for char in line:
            if char in "([{<":
                stack.append(char)
            else:
                if abs(ord(char) - ord(stack.pop())) > 3:
                    ans1 += points1[char]
                    break
        else:
            ans2.append(0)
            while stack:
                ans2[-1] = ans2[-1]*5 + points2[stack.pop()]
    print(ans1)
    print(sorted(ans2)[len(ans2)//2])

            


run("example.txt")
print()
run("day11.txt")