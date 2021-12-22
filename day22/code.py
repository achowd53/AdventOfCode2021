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

    lines = [re.match("(.*) x=(.*)\.\.(.*),y=(.*)\.\.(.*),z=(.*)\.\.(.*)", line).groups() for line in open(filename).read().splitlines()]
    lines = [(line[0],(int(line[1]),int(line[2])+1),(int(line[3]),int(line[4])+1),(int(line[5]),int(line[6])+1)) for line in lines]
    cubes = [] # A cube is define by ((xi,xf+1),(yi,yf+1),(zi,zf+1))
    def collide(cubeA, cubeB): # Check if cubes collide
        return max(cubeA[0][0],cubeB[0][0]) < min(cubeA[0][1],cubeB[0][1]) and\
                max(cubeA[1][0],cubeB[1][0]) < min(cubeA[1][1],cubeB[1][1]) and\
                max(cubeA[2][0],cubeB[2][0]) < min(cubeA[2][1],cubeB[2][1])
    def overlap(cubeA, cubeB): # Check where 2 cubes overlap
        return ((max(cubeA[0][0],cubeB[0][0]), min(cubeA[0][1],cubeB[0][1])),
                (max(cubeA[1][0],cubeB[1][0]), min(cubeA[1][1],cubeB[1][1])),
                (max(cubeA[2][0],cubeB[2][0]), min(cubeA[2][1],cubeB[2][1])))
    def subtract(cubeA, cubeB): # Subtract cubeB from cubeA and split cubeA into new cubes
        new_cubes = [((cubeA[0][0],cubeB[0][0]),cubeA[1],cubeA[2]), ((cubeB[0][1],cubeA[0][1]),cubeA[1],cubeA[2])]
        cubeA = ((max(cubeA[0][0],cubeB[0][0]),min(cubeA[0][1],cubeB[0][1])),cubeA[1],cubeA[2])
        new_cubes.extend([(cubeA[0],(cubeA[1][0],cubeB[1][0]),cubeA[2]), (cubeA[0],(cubeB[1][1],cubeA[1][1]),cubeA[2])])
        cubeA = (cubeA[0],(max(cubeA[1][0],cubeB[1][0]),min(cubeA[1][1],cubeB[1][1])),cubeA[2])
        new_cubes.extend([(cubeA[0],cubeA[1],(cubeA[2][0],cubeB[2][0])), (cubeA[0],cubeA[1],(cubeB[2][1],cubeA[2][1]))])
        return list((x,y,z) for x,y,z in new_cubes if x[0]<x[1] and y[0]<y[1] and z[0]<z[1])
    for reboot in lines:
        new_cubes = []
        for cubeA in cubes: # For every cube previously found, subtract the new cube from them
            if collide(cubeA, reboot[1:]): new_cubes.extend(subtract(cubeA, overlap(cubeA, reboot[1:])))
            else: new_cubes.append(cubeA)
        if reboot[0] == "on": new_cubes.append(reboot[1:]) # Add new cube to cubes if it's turning on
        cubes = new_cubes
    print(sum((math.prod(max(-50,min(50,cube[i][1]))-min(50,max(-50,cube[i][0])) for i in range(3)) for cube in cubes)))
    print(sum((x[1]-x[0])*(y[1]-y[0])*(z[1]-z[0]) for x,y,z in cubes))


run("example.txt")
print()
run("day22.txt")
