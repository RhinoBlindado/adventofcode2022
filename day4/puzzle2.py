import numpy as np
import string


"""
ADVENT OF CODE 2022

DAY 4 PUZZLE 2

"""


def checkIfOverlap(first, second):

    overlap = False    

    # Separate the literal string numbers.
    first  = first.split(sep="-")
    second = second.split(sep="-")

    # Convert them to type int and generate the number ranges.
    # - Since arange is not inclusive with the ending number, add +1.
    firstRange  = np.arange(int(first[0]), int(first[1])+1)
    secondRange = np.arange(int(second[0]), int(second[1])+1)

    # To check if one set overlaps another, one way is to make the ranges as
    # sets, and use the AND operator to check if both sets contain repeats.
    # If the resulting set as a length greater than 0, there's an overlap.

    if(len(set(firstRange) & set(secondRange)) > 0):
        overlap = True

    return overlap


#%% MAIN

# Load input

# PATH = "input_sample.txt"
PATH = "input.txt"

file = open(PATH, 'r')

#%%

totOverlaps = 0

# Loop the input...
for line in file:
    
    # Strip the line break and separate the pairs.
    firstElf, secondElf = line.strip().split(sep=",")
    
    # print("First Elf has {}, second has {}".format(firstElf, secondElf))
    
    # If there is overlap, count it.
    if(checkIfOverlap(firstElf, secondElf)):
        totOverlaps += 1
        # print("One is subset of the other.")

print("The number of overlaps is: {}".format(totOverlaps))    
    
file.close()