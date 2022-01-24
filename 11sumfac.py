#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

# your code goes here

n = 5
sum = 0
mult = 1
for i in range(1, (n+1)):
    sum += i
    mult *= i
print(i, sum, mult)

"""
python3 11sumfac.py
5 15 120
"""
