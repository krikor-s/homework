#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

caldays = 365
numtrials = 1000
people = 25
sharebday = 0

#loop for trials
for i in range(numtrials):
    calendar = []
    for j in range(caldays): #make list for calender
        calendar.append(0)
    for x in range(people): #assign 25 people a random # between 0 and 364
        calpos = random.randint(0, caldays - 1)
        calendar[calpos] = calendar[calpos] + 1
    for y in calendar: #check if there is shared bday
        if y > 1:
            sharebday += 1 #add to the shared amount of bdays
            break

print(f'{sharebday/numtrials:.3f}')

#worked with Paul and Jojo(Yaniel)
"""
python3 33birthday.py
0.571
"""

