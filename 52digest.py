#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments

# pull the gene code and label as seq
# pull the gaattc and mark that as a certain variable
# cross reference variable with seq to see if there are any matches
# record said matches and print position in sequence

afterorigin = False
seq = ''
with open(sys.argv[1]) as fp:
    for line in fp.readlines():
        if line.startswith("ORIGIN"):
            afterorigin = True
        if afterorigin:    
            words = line.split() # splits the line into words
            seq += "".join(words[1:]) # glues sequence together except for the number in front
            
restr = sys.argv[2]

start = [1]
for match in re.finditer(restr, seq):
    start.append(match.start())
start.append(len(seq))

for i in range(len(start)-1):
    x = start[i+1] - start[i]
    print(x)

# I worked with Paul

"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
