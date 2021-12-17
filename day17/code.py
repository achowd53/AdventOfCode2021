import numpy as np #np arrays are just nice in general
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

    x1, x2, y1, y2 = map(int, re.findall(r"-?\d+", open(filename).read().strip()))
    ans2 = 0
    for x in range(-max(abs(x1),abs(x2))-1,max(abs(x1),abs(x2))+1):
        for y in range(-max(abs(y1),abs(y2))-1,max(abs(y1),abs(y2))+1):
            pos, vel_x, vel_y = (0,0), x, y
            while pos[0] <= x2 and pos[1] >= y1:
                pos, vel_x, vel_y = (pos[0]+vel_x,pos[1]+vel_y), vel_x-(vel_x > 0)+(vel_x < 0), vel_y-1
                if x1 <= pos[0] <= x2 and y1 <= pos[1] <= y2:
                    ans2 += 1
                    break
    # vel_y = -vel_i_y at y = 0 so best case to not miss the target is vel_i_y = y1
    # max_height = sum from vel_i_y to 0 as drag is just -1 and at max_height, vel_y = 0
    print(y1*(y1+1)//2)
    print(ans2)
                    


run("example.txt")
print()
run("day17.txt")