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

    def solve_grid(lines):
        graph = networkx.Graph()
        for i in range(len(lines)):
            for j in range(len(lines)):
                graph.add_node((i,j), weight=lines[i][j])
        for i in range(1,len(lines)-1):
            for j in range(1,len(lines[0])-1):
                graph.add_edge((i,j),(i-1,j))
                graph.add_edge((i,j),(i+1,j))
                graph.add_edge((i,j),(i,j-1))
                graph.add_edge((i,j),(i,j+1))
        print(networkx.dijkstra_path_length(graph, (1,1), (len(lines)-2,len(lines[0])-2), weight=lambda u,v,d: graph.nodes[v].get("weight",1)))
    lines = open(filename).read().splitlines()
    lines = [[100]+list(map(int,list(line)))+[100] for line in lines]
    lines = [[100]*len(lines[0])] + lines + [[100]*len(lines[0])]
    solve_grid(lines)
    f = {1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:1}
    lines = open(filename).read().splitlines()
    lines = [list(map(int,list(line))) for line in lines]
    for i in range(len(lines)):
        lines[i] += list(f[x] for x in lines[i]) + list(f[f[x]] for x in lines[i]) + list(f[f[f[x]]] for x in lines[i]) + list(f[f[f[f[x]]]] for x in lines[i])
    lines += list([f[x] for x in line] for line in lines) + list([f[f[x]] for x in line] for line in lines) + list([f[f[f[x]]] for x in line] for line in lines) + list([f[f[f[f[x]]]] for x in line] for line in lines)
    lines = [[100]+line+[100] for line in lines]
    lines = [[100]*len(lines[0])] + lines + [[100]*len(lines[0])]
    solve_grid(lines)
run("example.txt")
print()
run("day15.txt")