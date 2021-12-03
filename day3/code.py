import numpy as np #np arrays are just nice in general
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
import collections #defaultdicts, maybe counters
import functools #use @functools.lru_cache(None) above a function to keep track of all inputs and speed it up
import string #ascii_uppercase, ascii_lowercase, etc..
import itertools #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
from copy import deepcopy #deepcopy() let's use copy a list without reference areas
#Sets are POG {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))

def run(filename):
    print("Running",filename+"...")

    lines = open(filename).read().splitlines()
    gamma = ""
    epsilon = ""
    oxygen = list(lines)
    co2 = list(lines)
    for i in range(len(lines[0])):
        common = collections.Counter(x[i] for x in lines).most_common()[0][0]
        gamma += common
        epsilon += "1" if common == "0" else "0"
        if len(oxygen) > 1:
            oxygen_common = collections.Counter(x[i] for x in oxygen)
            if oxygen_common["1"] == oxygen_common["0"]: oxygen_common = "1"
            else: oxygen_common = oxygen_common.most_common()[0][0]
            oxygen = [o for o in oxygen if o[i] == oxygen_common]
        if len(co2) > 1:
            co2_common = collections.Counter(x[i] for x in co2)
            if co2_common["1"] == co2_common["0"]: co2_common = "1"
            else: co2_common = co2_common.most_common()[0][0]
            co2 = [c for c in co2 if c[i] != co2_common]
    print(int(gamma,2)*int(epsilon,2))
    print(int(oxygen[0],2)*int(co2[0],2))

run("example.txt")
print()
run("day3.txt")