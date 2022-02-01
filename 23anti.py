#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
rdna = ''
for i in range(len(dna)):
    if dna[i] == "A":
        rdna += "T"
    elif dna[i] == "T":
        rdna += "A"
    elif dna[i] == "C":
        rdna += "G"
    elif dna[i] == "G":
        rdna += "C"
    
print(rdna[::-1])

# worked with Paul, Thomas, and Tiffany

"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
