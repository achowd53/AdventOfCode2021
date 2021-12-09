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

    lines = open(filename).read().splitlines()
    ans1, ans2 = 0, 0
    map = {'abcdefg':'8','bcdef':'5','acdfg':'2','abcdf':'3','abd':'7','abcdef':'9','bcdefg':'6','abef':'4','abcdeg':'0','ab':'1'}
    for line in lines:
        a,b = line.split(' | ')
        a,b = a.split(),b.split()
        ans1 += sum(1 for k in b if len(k) in [2,3,4,7])
        for perm in itertools.permutations("abcdefg"):
            let = {i:j for i,j in zip("abcdefg",perm)}
            tem = [''.join(sorted([let[i] for i in j])) for j in a]
            out = [''.join(sorted([let[i] for i in j])) for j in b]
            if all(k in map for k in tem):
                ans2 += int(''.join(map[j] for j in out))
                break
    print(ans1)
    print(ans2)


run("example.txt")
print()
run("day8.txt")