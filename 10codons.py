#!/usr/bin/env python3


# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop
# your code goes here

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'
k = 3
for i in range(0, len(dna), k):
    print(dna[i:i+k])

# I worked with Paul
"""
python3 10codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
