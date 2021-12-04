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
    lines = open(filename).read().split("\n\n")
    lines = [line.replace("\n"," ") for line in lines]
    boards = [re.sub(' +',' ',line.strip()).split() for line in lines[1:]]
    called = lines[0].split(",")
    def win(board, called):
        for a,b,c,d,e in [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24],[0,5,10,15,20],[1,6,11,16,21],[2,7,12,17,22], [3,8,13,18,23],[4,9,14,19,24]]:
            if board[a] in called and board[b] in called and board[c] in called and board[d] in called and board[e] in called:
                return True
        return False
    current = set()
    num_won = 0
    for ball in called:
        current.add(ball)
        for b in range(len(boards)):
            board = boards[b]
            if board == "w": continue
            if win(board,current):
                x = sum(int(i) for i in set(board) - current)
                if num_won == 0 or num_won == len(boards) - 1: print(x * int(ball))
                boards[b] = "w"  
                num_won += 1 

run("example.txt")
print()
run("day4.txt")