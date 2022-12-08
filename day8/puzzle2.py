# Double-Ended Queues
from collections import deque

import numpy as np
"""
ADVENT OF CODE 2022

DAY 8 PUZZLE 2

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
    
    visible = [0, 0, 0, 0]
    
    maxSize = visMap.shape[0]
    
    # Count each tree that appears before the highest tree found or the edge
    # Check up from tree to margin.
    for i in range(0, x):
        visible[0] += 1
        if(treeMap[(x-1)-i][y] >= treeMap[x,y]):
            break
    
    # Check down...
    for i in range(x+1, maxSize):
        visible[1] += 1
        if(treeMap[i, y] >= treeMap[x, y]):
            break

    # Check left...
    for j in range(0, y):
        visible[2] += 1
        if(treeMap[x, (y-1)-j] >= treeMap[x, y]):
            break

    # Check right...
    for j in range(y+1, maxSize):
        visible[3] += 1
        if(treeMap[x, j] >= treeMap[x, y]):
            break

    # Calculate the scenic score.
    return visible[0] * visible[1] * visible[2] * visible[3]
    

#%% MAIN
# Load input
# PATH = "input_sample.txt"
PATH = "input.txt"

file = open(PATH, 'r')

# Read the file as a number matrix.
treeMap = fillMap(file)

file.close()

#%%

# Put the visibility map at zero.
treeMap = np.array(treeMap)
visMap  = np.zeros(treeMap.shape)
   
height, witdh = treeMap.shape

#%%

for i in range(1, height-1):
    for j in range(1, witdh-1):
        visMap[i,j] = checkIfVisible(i,j,treeMap)

print("There highest scenic score is {}".format(np.max(visMap)))