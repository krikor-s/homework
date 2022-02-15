#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

#appending numbers in command line
arr1 = []
for i in range(1, len(sys.argv)):
    arr1.append(int(sys.argv[i]))

#count, min, max
arr1.sort()
Count = len(arr1) #count done
Minimum = arr1[0]  #min done
Maximum = arr1[len(arr1)-1] #max done

#mean calc
add = 0
for i in range(len(arr1)):
    add += arr1[i]
Mean = add/len(arr1) #mean done

#std calc
Standev0 = 0
for i in range(len(arr1)):
    Standev0 += (arr1[i]-Mean)**2 #can't put whole formula in loop it will mess it up
Standev1 = math.sqrt(Standev0/Count) #second part of formula
#std done

#mdn calc
if Count % 2 == 1: 
    Median1 = arr1[math.floor(Count/2)]
else:    
    med1 = arr1[Count/2 - 1]
    med2 = arr1[Count/2]
    Median1 = (med1 + med2)/2 #med done

print('Count:', Count) 
print('Minimum:', f'{Minimum:.1f}')
print('Maximum:', f'{Maximum:.1f}')
print('Mean:', f'{Mean:.3f}')
print('Std. dev:', f'{Standev1:.3f}') 
print('Median:', f'{Median1:.3f}')

# I worked with Paul and Jojo(Yaniel)
"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
