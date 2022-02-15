#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

#appending numbers in command line
probability = [] #appended line'
sum = 0
for i in range(1, len(sys.argv)):
    probability.append(float(sys.argv[i]))
    sum += float(sys.argv[i])

#must be = to around 1
allow = 0.01
if abs(sum-0.1) > allow:
    print("doesn't work")
    sys.exit() #seen in lecture
#maintains 1 with dif values in command line

#entropy calc
ent = 0
for i in probability:
    ent += -sum*i*math.log2(i) #entropy calc done
print(f'{ent:.3f}')


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
