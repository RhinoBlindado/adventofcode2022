import argparse 
import sys
import numpy as np

"""
ADVENT OF CODE 2022

DAY 2 PUZZLE 1

"""

def getScore(opponent, player):
    
    score = 0
    
    if(opponent == "A"):
        if(player == "X"):
            score = 3
        elif(player == "Y"):
            score = 6
        
    if(opponent == "B"):
        if(player == "Y"):
            score = 3
        elif(player == "Z"):
            score = 6
        
    if(opponent == "C"):
        if(player == "Z"):
            score = 3
        elif(player == "X"):
            score = 6
            
    return score
        

scoreDict = {"X" : 1,
             "Y" : 2,
             "Z" : 3}


# Rock:     A X
# Paper:    B Y
# Scissors: C Z


PATH = "input.txt"

file = open(PATH, 'r')

totalScore = 0

for line in file:
    
    
    opnt, plyr = line.split()

    roundScore = getScore(opnt, plyr) + scoreDict[plyr]
    # print("Round score is {}".format(roundScore))
    totalScore += roundScore
    
    
print("The total score is {}".format(totalScore))
    
    

