from networkx.algorithms.centrality.group import prominent_group
import numpy as np #np arrays are just nice in general
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
import collections #defaultdicts, maybe counters
import functools #use @functools.lru_cache(None) above a function to keep track of all inputs and speed it up
import string #ascii_uppercase, ascii_lowercase, etc..
import itertools #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
import networkx #Networkx for graph problems
from copy import deepcopy #deepcopy() let's use copy a list without reference areas
#Sets are POG {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))

def run(filename):
    print("Running",filename+"...")

    smoke = [list(map(int,[9]+list(line)+[9])) for line in open(filename).read().splitlines()]
    smoke = [[9]*len(smoke[0])] + smoke + [[9]*len(smoke[0])]
    risk = 0
    graph = networkx.Graph()
    for i in range(1,len(smoke)-1):
        for j in range(1,len(smoke[0])-1):
            if smoke[i][j] != 9:
                if all(smoke[i][j] < smoke[x][y] for x,y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]):
                    risk += smoke[i][j] + 1
                for x,y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if smoke[x][y] != 9:
                        graph.add_edge((i,j),(x,y))
    basins = sorted([len(basin) for basin in networkx.connected_components(graph)])
    print(risk)
    print(basins[-1]*basins[-2]*basins[-3])


run("example.txt")
print()
run("day9.txt")