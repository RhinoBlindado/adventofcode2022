import numpy as np
import string


"""
ADVENT OF CODE 2022

DAY 3 PUZZLE 1

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

# Loop the input...
for line in file:
    
    # Get the line lenght without the line break
    lenLine = len(line[0:-1])
    
    # Get the first and second halves...
    firstHalf = line[0:lenLine//2]
    secondHalf = line[(lenLine//2):lenLine]
    
    # Using a set get the only item that is repeated in both halves.
    repeatedItem = set(firstHalf) & set(secondHalf)
    
    # Use the dictionary to get its priority and sum it.
    totPriority += priority[repeatedItem.pop()]


print("The sum of the priorities of the repeated items is {}.".format(totPriority))    
    
    