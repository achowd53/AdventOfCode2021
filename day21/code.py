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

def run(filename):
    print("Running",filename+"...")
    
    lines = [int(line.split(': ')[1]) for line in open(filename).readlines()]
    pos, scores, dice_rolls = lines[:], [0,0], 0
    while max(scores) < 1000:
        for i in range(2):
            pos[i] = (pos[i]+(6+3*dice_rolls)-1)%10 + 1
            scores[i] += pos[i]
            dice_rolls += 3
            if pos[i] >= 1000: break
    print(min(scores)*dice_rolls)
    @functools.lru_cache(None)
    def universe(pos1, pos2, score1, score2):
        if score1 >= 21: return np.array((1,0), dtype="int64")
        if score2 >= 21: return np.array((0,1), dtype="int64")
        return sum(universe(pos2, (pos1+i+j+k-1)%10+1, score2, score1+(pos1+i+j+k-1)%10+1)[::-1] 
                   for i,j,k in itertools.product([1,2,3], repeat=3))
    print(max(universe(lines[0], lines[1], 0, 0)))

run("example.txt")
print()
run("day21.txt")