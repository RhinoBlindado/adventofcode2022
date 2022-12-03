import numpy as np
import string


"""
ADVENT OF CODE 2022

DAY 3 PUZZLE 2

"""

def genDict():
    
    # Get the whole abecedary in lower and uppercase.
    lowerCase = string.ascii_lowercase
    upperCase = string.ascii_uppercase
    
    scoreDict = {}
    
    # Fill the dictionary, each letter mapping to 1 thru 26...
    for pri, lett in enumerate(lowerCase):
        scoreDict[lett] = pri + 1
        
    # and 27 up to 52.
    for pri, lett in enumerate(upperCase):
        scoreDict[lett] = pri + 27
        
    return scoreDict

#%% MAIN

# Load input

# PATH = "input_sample.txt"
PATH = "input.txt"

file = open(PATH, 'r')

# Generate dictionary to map each letter to a number.
priority = genDict()

# Declare accumulator variable.
totPriority = 0

# Load the whole input into a list.
inputLines = file.readlines()

#%%
# Loop the list in steps of 3, for the 3 groups of elves...
for i in range(0, len(inputLines), 3):
    # Using a set get the only item that is repeated in each group of three
    # - The line break is removed first.
    repeatedItem = set(inputLines[i][:-1]) & set(inputLines[i+1][:-1]) & set(inputLines[i+2][:-1])
    
    # Use the dictionary to get its priority and sum it.
    totPriority += priority[repeatedItem.pop()]


print("The sum of the priorities of the items is {}.".format(totPriority))    


file.close()
    