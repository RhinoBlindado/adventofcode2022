import numpy as np
import string


"""
ADVENT OF CODE 2022

DAY 4 PUZZLE 1

"""

def checkIfSubset(first, second):

    isSubset = False    

    # Separate the literal string numbers.
    first  = first.split(sep="-")
    second = second.split(sep="-")

    # Convert them to type int and store them in pairs.
    firstRange  = (int(first[0]), int(first[-1]))
    secondRange = (int(second[0]), int(second[-1]))

    # To check if one range is subset of the other:
    """
    - Check if the starting range number is less or equal than the other starting number
    and the ending number is greather or equal than the other. Both ways.
     
    Example: 
    
    ..12345..
    ...234...
    
    or
    
    ...234...
    ..12345..
    
    """

    if((firstRange[0] <= secondRange[0] and
       firstRange[1] >= secondRange[1]) or
       (secondRange[0] <= firstRange[0] and
        secondRange[1] >= firstRange[1])):
        isSubset = True
        
    return isSubset


#%% MAIN

# Load input

#PATH = "input_sample.txt"
PATH = "input.txt"

file = open(PATH, 'r')

#%%

totSubsets = 0

# Loop the input...
for line in file:
    
    # Strip the line break and separate the pairs.
    firstElf, secondElf = line.strip().split(sep=",")
    
    # print("First Elf has {}, second has {}".format(firstElf, secondElf))
    
    # If one is subset of the other, count it.
    if(checkIfSubset(firstElf, secondElf)):
        totSubsets += 1
        # print("One is subset of the other.")

print("The number of subsets is: {}".format(totSubsets))    
    
file.close()