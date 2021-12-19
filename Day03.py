#Advent of Code 2015 - Day 3
import os

#Reading the puzzle text file from your Windows Desktop folder
with open(os.environ['USERPROFILE'] + r'\Desktop\Advent of Code\2015\input03.txt', 'r') as f:
    data = f.read()

def get_position(i, j, k):
    if k == 'v':
        return i+1, j
    elif k == '^':
        return i-1, j
    elif k == '>':
        return i, j+1
    else:
        return i, j-1

#First part
houses = []
x, y = 0, 0
for sign in data:
    x, y = get_position(x, y, sign)
    if (x,y) not in houses:
        houses.append((x,y))
print(len(houses))

#Second part
houses = [(0,0)]
x, y, rx, ry = 0, 0, 0, 0
for idx, sign in enumerate(data):
    if idx % 2 == 0: 
        x, y = get_position(x, y, sign)
        if (x,y) not in houses:
            houses.append((x,y))
    else:
        rx, ry = get_position(rx, ry, sign)
        if (rx,ry) not in houses:
            houses.append((rx,ry))
print(len(houses))