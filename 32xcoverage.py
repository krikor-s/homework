#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random
arr = []
for i in range(1, len(sys.argv)): #pulls from command line
    arr.append(int(sys.argv[i]))

gensize = arr[0] #1000 - var for size
rednum = arr[1] #100 - var for num
redlen = arr[2] #100 - var for len

#set up for number of reads
for i in range(rednum):
    genlist = [] #make list for genome
    for j in range(gensize):
        genlist.append(0) #genome list done
for x in range(rednum): #addition if read
    redpos = random.randint(0, gensize-redlen)
    for i in range(redlen):
        genlist[i + redpos] += 1

#report #s
genlist.sort() #aligns list
min = genlist[0 + redlen] #ignores beginning sample
max = genlist[gensize - redlen] #ignores end sample
sum = 0
for i in genlist[redlen:-redlen]: #helps avg
    sum += i

print(min, max, f'{sum/(gensize-2*redlen):.5f}')

#worked with Paul and Jojo(Yaniel)
"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
