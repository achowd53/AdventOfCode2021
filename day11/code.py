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
   
    grid = np.array([list(map(int,list(line))) for line in open(filename).read().splitlines()]).reshape(100,)
    flashes = 0
    for step in range(1,1000):
        flashed = np.zeros((100), dtype=bool)  
        grid += 1        
        new_flash = (grid > 9)
        while np.any(new_flash):
            flashed |= new_flash                  
            for idx in np.where(new_flash)[0]:
                for i in [-11,-10,-9,-1,1,9,10,11]:
                    if abs(idx%10-(idx+i)%10)+abs(idx//10-(idx+i)//10) < 3 and -1 < idx+i < 100:
                        grid[i+idx] += 1
            new_flash = (grid > 9) & (~flashed)
        grid[flashed] = 0
        if step < 101: flashes += np.sum(flashed)
        if np.all(grid==0): break
    print(flashes)
    print(step)

run("example.txt")
print()
run("day11.txt")