import scipy.ndimage as sp, numpy as np #np arrays are just nice in general and scipy.ndimage correlate and convolve
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

    lines = [list(line.strip()) for line in open(filename).readlines()]
    step = 0
    while True:
        moves = 0
        step += 1
        new_moves = []
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                if lines[y][x] == ">" and lines[y][(x+1)%len(lines[0])] == ".":
                    moves += 1
                    new_moves.append((y,x))
        for y,x in new_moves:
            lines[y][x] = "."
            lines[y][(x+1)%len(lines[0])] = ">"
        new_moves = []
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                if lines[y][x] == "v" and lines[(y+1)%len(lines)][x] == ".":
                    moves += 1
                    new_moves.append((y,x))
        for y,x in new_moves:
            lines[y][x] = "."
            lines[(y+1)%len(lines)][x] = "v"
        if moves == 0:
            print(step)
            break


run("example.txt")
print()
run("day25.txt")

