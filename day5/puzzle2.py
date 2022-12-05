# Optimized stacks
from collections import deque

"""
ADVENT OF CODE 2022

DAY 5 PUZZLE 2

"""

def genStacks(rawInput):
    """
    Parse the raw input.

    """
    
    # Split the file.
    bottomLine = rawInput[-1]
    contents   = rawInput[:-1]
    
    stackIdx = []
    stacks   = []
    
    # - Loop over the bottom line, which contains the number of stacks.
    for i, char in enumerate(bottomLine):
        # - Save the string index in which a number is found, and create an empty stack
        # object.
        if(char != " "):
            stackIdx.append(i)
            stacks.append(deque())
    
    # print(stackIdx)
    
    # For each row of the contents...
    for row in contents:
        
        # Loop over the stack indices...
        for sIdx, rowIdx in enumerate(stackIdx):
            
            # - If the string index from the bottom row matches with something
            # that's not a space or out of bounds, then it's part of that stack.
            # - Add it to the corresponding stack, the i-th stack of the list.
            try:
                if (row[rowIdx] != " "):
                    stacks[sIdx].appendleft(row[rowIdx])
            except Exception:
                pass
    
    # print(stacks)
    return stacks

#%% MAIN

# Load input
# PATH = "input_sample.txt"
PATH = "input.txt"

file = open(PATH, 'r')

#%%

stackConfig = []
stackMoves  = []

headerFound = False
# Loop the input...
for line in file:
    
    # If before the line break, it's part of the stack configuration. 
    # - Save it with spaces but not the ending line break.
    # - Save the rest in another list, remove the strings since those don't
    # add any important info. Save only the numbers.
    if not headerFound:
        if(line == "\n"):
            headerFound = True
        else:
            stackConfig.append(line[:-1])
    else:
        stackMoves.append(line[:-1].split()[1::2])

#%%

# Generate stacks based on the raw input.
stacks = genStacks(stackConfig)

#%%

# For each instruction in the list...
for move in stackMoves:
    
    # Get the crates to move, the stack of origin and destination.
    cratesToMove = int(move[0])
    origStack    = int(move[1]) - 1
    destStack    = int(move[2]) - 1
    
    # Get the number of crates already in the stack.
    numCratesDest = len(stacks[destStack])
    # Move the number of crates from the origin to destination.
    for i in range(0, cratesToMove):
        # To make it in the same order, append to the left instead of the right.
        # This naturally shifts the original crates to the right.
        stacks[destStack].appendleft(stacks[origStack].pop())
    
    # Rotate, that is, shift the crates so that they move to their original
    # postition, but with the added crates on top and in order.
    stacks[destStack].rotate(numCratesDest)
    
# Save the tops of the stacks and show to screen.
top = ""
for stck in stacks:
    top += stck.pop()
    
print("After rearrangement, the top of the stacks are {}".format(top))
    
#%%
file.close()