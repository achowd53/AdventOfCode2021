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

    graph = networkx.Graph()
    for line in open(filename).read().splitlines():
        a,b = line.split('-')
        graph.add_edge(a,b)
    
    def search(path, part1):
        if path[-1] == "end": yield path
        for node in list(graph.neighbors(path[-1])):
            recaved = part1
            if node.islower() and node in path:
                if recaved: continue
                else:
                    if node in ["start","end"]:
                        continue
                    recaved = True
            yield from search(path+[node], recaved)
    print(len(list(search(['start'], True))))
    print(len(list(search(['start'], False))))
    
run("example.txt")
print()
run("day12.txt")