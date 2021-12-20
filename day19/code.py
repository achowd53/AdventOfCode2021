import numpy as np #np arrays are just nice in general
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
import collections #defaultdicts, maybe counters
import functools #use @functools.lru_cache(None) above a function to keep track of all inputs and speed it up
import math, string #ascii_uppercase, ascii_lowercase, etc..
import itertools #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
from copy import deepcopy #deepcopy() let's use copy a list without reference areas
#Sets are POG {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))

def run(filename):
    print("Running",filename+"...")

    lines = open(filename).read().split('\n\n')
    scanner_data = dict()
    i = 0
    for line in lines:
        line = line.split('\n')
        line = [line[0]] + [list(map(int,beacon.split(','))) for beacon in line[1:]]
        scanner_data.update({i: np.array(line[1:])})
        i += 1
    def orientations(beacon_coords):
        out = []
        for x in beacon_coords:
            a,b,c = x
            z = [(a,b,c),(b,c,a),(c,a,b),(c,b,-a),(b,a,-c),(a,c,-b),(a,-b,-c),(b,-c,-a),(c,-a,-b),(c,-b,a),(b,-a,c),(a,-c,b),(-a,b,-c),(-b,c,-a),(-c,a,-b),(-c,b,a),(-b,a,c),(-a,c,b),(-a,-b,c),(-b,-c,a),(-c,-a,b),(-c,-b,-a),(-b,-a,-c),(-a,-c,-b)]
            out.append(z)
        return list(np.array(x) for x in zip(*out))
    def match(scanner_a, rotation_b):
        freq = collections.defaultdict(int)
        for a in scanner_data[scanner_a]:
            for b in rotation_b:
                freq[(b[0]-a[0],b[1]-a[1],b[2]-a[2])] += 1
                if freq[(b[0]-a[0],b[1]-a[1],b[2]-a[2])] == 12:
                    return (b[0]-a[0],b[1]-a[1],b[2]-a[2])
        return None
    common_beacons = set(tuple(tuple(x) for x in np.array(scanner_data[0])))
    scanner_locs = {0:(0,0,0)}
    while len(scanner_locs) != len(scanner_data):
        for a in set(range(len(scanner_data)))-set(scanner_locs):
            for b in scanner_locs:
                for orientation in orientations(scanner_data[a]):
                    if match(b,orientation):
                        scanner_locs[a] = tuple(np.array(scanner_locs[b]) + np.array(match(b,orientation)))
                        scanner_data[a] = list(list(x) for x in orientation)
                        common_beacons |= set(tuple(x) for x in np.array(orientation)-np.array(scanner_locs[a]))
                        break
                else: continue
                break
    print(len(common_beacons))
    max_manhattan = 0
    for a in scanner_locs.values():
        for b in scanner_locs.values():
            max_manhattan = max(max_manhattan, abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2]))
    print(max_manhattan)
run("example.txt")
print()
run("day19.txt")