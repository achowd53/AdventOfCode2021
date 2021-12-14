
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

    dots, folds = open(filename).read().split("\n\n")
    dots = set(tuple(map(int, dot.split(','))) for dot in dots.split('\n'))
    folds = [tuple(fold.split('=')) for fold in folds.split('\n')]
    folds = [(fold[0][-1], int(fold[1])) for fold in folds]
    for i,(dir,val) in enumerate(folds):
        new_dots = set()
        for x,y in dots:
            if dir == 'y': x,y = y,x 
            if x > val: x = val*2-x
            if dir == 'x': new_dots.add((x,y))
            else: new_dots.add((y,x))
        dots = new_dots
        if i == 0: print(len(dots))
    for y in range(min(dots, key=lambda x:x[1])[1], max(dots,key=lambda x:x[1])[1]+1):
        for x in range(min(dots, key=lambda x:x[0])[0], max(dots,key=lambda x:x[0])[0]+1):
            print('.' if (x,y) in dots else ' ', end='')
        print()

run("example.txt")
print()
run("day13.txt")