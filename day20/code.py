import scipy.ndimage as sp, numpy as np #np arrays are just nice in general
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
import collections #defaultdicts, maybe counters
import functools #use @functools.lru_cache(None) above a function to keep track of all inputs and speed it up
import math, string #ascii_uppercase, ascii_lowercase, etc..
import itertools #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
import networkx #Networkx for graph problems like connected components
from copy import deepcopy #deepcopy() let's use copy a list without reference areas
#Sets are POG {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))

def run(filename, swap=False):
    print("Running",filename+"...")

    lines = open(filename).read().split('\n\n')
    algorithm = [i for i in range(len(lines[0])) if lines[0][i] == "#"]
    image = np.pad(np.array([[1 if c == "#" else 0 for c in line] for line in lines[1].split('\n')]), pad_width=60)
    binary = np.array([[256,128,64],[32,16,8],[4,2,1]])
    for i in range(50):
        if i == 2: print(np.sum(image))
        image = np.isin(sp.correlate(image,binary,mode='constant',cval=(i%2 if swap else 0)), algorithm).astype(int)
    print(np.sum(image))

run("example.txt")
print()
run("day20.txt", True)