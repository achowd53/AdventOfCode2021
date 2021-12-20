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

    def explode(x, i=4):
        if isinstance(x, int): return False, x
        if i == 0: return True, 0
        a,b = x
        exploded, a = explode(a, i-1)
        if exploded: return True, [a,b]
        exploded, b = explode(b, i-1)
        if exploded: return True, [a,b]
        return False, [a,b]
    def split(x):
        if isinstance(x, int):
            if x >= 10: return True, [x//2,(x+1)//2]
            else: return False, x
        a,b = x
        splitted, a = split(a)
        if splitted: return True, [a,b]
        splitted, b = split(b)
        if splitted: return True, [a,b]
        return False, [a,b]
    def check(a,b):
        snailfish = [a,b]
        while True:
            exploded, fishsnail = explode(snailfish)
            if exploded:
                str1, str2, idx = str(snailfish), str(fishsnail), 0
                for i in range(len(str1)):
                    if str1[i] != str2[i]:
                        idx = i
                        break
                add_left, add_right = map(int, str1[idx+1:idx+str1[idx:].find(']')].split(', '))
                while not str1[i].isdigit(): i -= 1
                temp = ''
                while str1[i].isdigit():
                    temp = str1[i] + temp
                    i -= 1
                if temp: str2 = str(int(temp)+add_left).join(str1[:idx].rsplit(temp,1)) + str2[idx:]
                idx += len(str(int(temp)+add_left))-1
                while idx+1 < len(str2)-1 and not str2[idx+1].isdigit(): idx += 1
                temp = ''
                tidx = idx
                while str2[tidx+1].isdigit():
                    temp += str2[tidx+1]
                    tidx += 1
                if temp: str2 = str2[:idx+1] + str2[idx+1:].replace(temp, str(int(temp)+add_right), 1)
                snailfish = eval(str2)
                continue
            splitted, snailfish = split(snailfish)
            if splitted: continue
            break
        return snailfish
    def magnitude(snailfish):
        if isinstance(snailfish, int): return snailfish
        else: return 3*magnitude(snailfish[0])+2*magnitude(snailfish[1])
    lines = [eval(line) for line in open(filename).read().splitlines()]
    x = functools.reduce(check, lines)
    print(magnitude(x))
    max_magnitude = 0
    for perm in itertools.permutations(lines,2):
        max_magnitude = max(max_magnitude, magnitude(check(*perm)))
    print(max_magnitude)

run("example.txt")
print()
run("day18.txt")