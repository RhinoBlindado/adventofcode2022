# Double-Ended Queues
from collections import deque

import numpy as np
"""
ADVENT OF CODE 2022

DAY 8 PUZZLE 1

"""

def fillMap(FILE):
    
    treeMap = []
    for line in FILE:        
        row = []
        for char in line.strip():
            row.append(int(char))
        treeMap.append(row)
    return treeMap

def checkIfVisible(x, y, treeMap):
    
    # Initialize the visibility from all the sides
    visible = [True, True, True, True]
    
    maxSize = visMap.shape[0]
    
    # Check up from tree to margin.
    for i in range(0, x):
        # If a tree is taller than or equal than actual tree, 
        # mark this tree as not visible from this side.
        if(treeMap[(x-1)-i][y] >= treeMap[x,y]):
            visible[0] = False
            break
    
    # Check down...
    for i in range(x+1, maxSize):
        if(treeMap[i, y] >= treeMap[x, y]):
            visible[1] = False
            break
        
    # Check left...
    for j in range(0, y):
        if(treeMap[x, (y-1)-j] >= treeMap[x, y]):
            visible[2] = False
            break
        
    # Check right...
    for j in range(y+1, maxSize):
        if(treeMap[x, j] >= treeMap[x, y]):
            visible[3] = False
            break
    
    # If all sides are "False", outputs False, if there's at least one "True"
    # returns true, so if there's only on side visible, the tree is visible.
    return np.max(visible)
    

#%% MAIN
# Load input
# PATH = "input_sample.txt"
PATH = "input.txt"

file = open(PATH, 'r')

# Read the file as a number matrix.
treeMap = fillMap(file)

file.close()

#%%

# Create a boolean array to save if a tree is visible.
treeMap = np.array(treeMap)
visMap  = np.full(treeMap.shape, False)

# The edge of the map are all visible.
visMap[:,0]  = True
visMap[:,-1] = True
visMap[0,:]  = True
visMap[-1, :]= True
   
height, witdh = treeMap.shape

#%%

# Loop for each tree inside the matrix, ignoring the margin of the matrix.
for i in range(1, height-1):
    for j in range(1, witdh-1):
        visMap[i,j] = checkIfVisible(i,j,treeMap)

print("There are {} trees visible from the outside".format(np.count_nonzero(visMap)))