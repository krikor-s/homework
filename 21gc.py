#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
numG = 0
numC = 0
numGC = 0
x = 1
for i in range(len(dna)):
    if dna[i] == "G":
         numGC += x
    if dna[i] == "C":
        numGC += x

print('{:.2f}'.format(numGC/len(dna))) 
print('%.2f' % (numGC/len(dna)))
print(f'{numGC/len(dna):.2f}')


"""
python3 21gc.py
0.42
0.42
0.42
"""
