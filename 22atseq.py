#!/usr/bin/env python3

import random

# random.seed(1) 
# comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

dna = ''
numAT = 0

random.seed(1)
for i in range(30):
    if random.random() < 0.6:
        numAT += 1
        if random.random() > 0.5:
            dna += "A"
        else:
            dna += "T"
    else:
        if random.random() > 0.5:
            dna += "G"
        else:
            dna += "C"
print(len(dna), numAT/len(dna), dna)

# worked with Paul, Thomas, and Tiffany

"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
