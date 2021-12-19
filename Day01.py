#Advent of Code 2015 - Day 1
import os
from collections import Counter

#Reading the puzzle text file (named as input01.txt) from your Windows Desktop folder
with open(os.environ['USERPROFILE'] + r'\Desktop\input01.txt', 'r') as f:
    data = [line for line in f.read()]

#First part
print(Counter(data)['('] - Counter(data)[')'])

#Second part
nopen, nclose = 0, 0
for i, item in enumerate(data, 1):
    if item == '(':
        nopen += 1
    else:
        nclose += 1
    if nopen - nclose == -1:
        break
print(i)
