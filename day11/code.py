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

    #lines = open(filename)
    #lines = open(filename).read().split('\n\n')
    octo = np.array([list(map(int,list(line))) for line in open(filename).read().splitlines()])
    flash = 0
    for step in range(1,1000):
        octo += 1
        flashed = set()
        new_flash = True
        while new_flash:
            new_flash = False
            for i in range(len(octo)):
                for j in range(len(octo[0])):
                    if octo[i][j] > 9 and (i,j) not in flashed:
                        new_flash = True
                        flash += 1
                        flashed.add((i,j))
                        for x,y in itertools.product([-1,0,1],[-1,0,1]):
                            if x == 0 and y == 0: continue
                            if -1 < i+y < len(octo) and -1 < j+x < len(octo[0]):
                                octo[i+y][j+x] += 1
        for x,y in flashed: octo[x][y] = 0
        if step == 100: print(flash)
        if octo[octo == 0].shape[0] == 100:
            print(step)
            break


run("example.txt")
print()
run("day11.txt")