#!/usr/bin/env python3
import collections
from collections import Counter

#niz = 'vztjeztreverpeep'
niz = 'asjlrlmbšrčntjbm'

filename='slovenske-besede.txt'


with open(filename) as f:
    lines = f.read().splitlines() 

letters = [*niz]
for l in lines:
    line_of_dic = [*l]
    ltrs = Counter(letters)
    lod = Counter(line_of_dic)
    if (lod-ltrs) == Counter():
        if len(l)>2:
            print(l)


