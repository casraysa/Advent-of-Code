#Advent of Code 2015 - Day 2
import os

def split_int(input_list):
    return [int(char) for char in input_list]

#Reading the puzzle text file from your Windows Desktop folder
with open(os.environ['USERPROFILE'] + r'\Desktop\Advent of Code\2015\input02.txt', 'r') as f:
    data = [split_int(line.strip().split('x')) for line in f.readlines()]

def get_paper_feet(l, w, h):
    return 2*(l*w+w*h+h*l) + min(l*w,w*h,h*l)

def get_ribon_feet(l, w, h):
    aux = sorted([l,w,h])
    return l*w*h + 2 * aux[0] + 2 * aux[1]

#First part
ans1 = 0
for i in data:
    ans1 += get_paper_feet(i[0],i[1],i[2])    
print(ans1)

#Second part
ans2 = 0
for i in data:
    ans2 += get_ribon_feet(i[0],i[1],i[2])
print(ans2)