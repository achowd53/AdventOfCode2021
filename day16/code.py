import numpy as np #np arrays are just nice in general
import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
import collections #defaultdicts, maybe counters
import functools #use @functools.lru_cache(None) above a function to keep track of all inputs and speed it up
import math, string #product, ascii_uppercase, ascii_lowercase, etc..
import itertools #itertools.product(range(a),range(b),[1,2,3]) allows for nested for loops in one line essentially
import networkx #Networkx for graph problems like connected components
from copy import deepcopy #deepcopy() let's use copy a list without reference areas
#Sets are POG {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Python has complex numbers of the form x+yj (1+1j) or complex(x,y) (complex(1,1))

def run(filename):
    print("Running",filename+"...")

    hex = open(filename).read().strip()
    binary = str(bin(int(hex,16)))[2:].zfill(len(hex)*4)
    operations = {0:sum, 1:math.prod, 2:min, 3:max, 5:lambda x: x[0]>x[1], 6:lambda x: x[0]<x[1], 7:lambda x: x[0]==x[1]}
    ans1 = set()
    def parsePacket(idx):
        nonlocal ans1
        V, T, idx = int(binary[idx:idx+3], 2), int(binary[idx+3:idx+6], 2), idx+6
        ans1.add((idx,V))
        if T == 4:
            value = ""
            while binary[idx] != "0":
                value += binary[idx+1:idx+5]
                idx += 5
            value += binary[idx+1:idx+5]
            idx += 5
            value = int(value, 2)
            return idx, value
        else:
            I, idx = int(binary[idx]), idx+1
            sub_packets = []
            if I == 0:
                total_sub_packet_length = int(binary[idx:idx+15], 2)
                idx += 15
                end = idx + total_sub_packet_length
                while idx < end:
                    try: idx, sub = parsePacket(idx)
                    except: break
                    sub_packets.append(sub)
            elif I == 1:
                num_sub_packets, idx = int(binary[idx:idx+11], 2), idx+11
                for _ in range(num_sub_packets):
                    idx, sub = parsePacket(idx)
                    sub_packets.append(sub)
            return idx, operations[T](sub_packets)
    _, sub_packets = parsePacket(0)
    print(sum(i[1] for i in ans1))
    print(sub_packets)
            


run("example.txt")
print()
run("day16.txt")