import argparse 
import sys
import numpy as np

"""
ADVENT OF CODE 2022

DAY 2 PUZZLE 2

"""

def getScore(opponent, player):
    
    score = 0
    
    if(player == "X"):
        score = scoreDict[losesOver[opponent]]
    elif(player == "Z"):
        score = scoreDict[winsOver[opponent]] + 6
    else:
        score = scoreDict[opponent] + 3
    
    return score
        

scoreDict = {"A" : 1,
             "B" : 2,
             "C" : 3}

winsOver = {"A" : "B", "B" : "C", "C" : "A"}
losesOver = {"A": "C", "B" : "A", "C" : "B"}

"""
Code:
-----
Rock:     A
Paper:    B
Scissors: C

Draw:     Y
Lose:     X
Win:      Z

"""

# PATH = "input_sample.txt"
PATH = "input.txt"

file = open(PATH, 'r')

totalScore = 0

for line in file:
    
    
    opnt, plyr = line.split()

    roundScore = getScore(opnt, plyr)
    # print("Round score is {}".format(roundScore))
    totalScore += roundScore
    
    
print("The total score is {}".format(totalScore))
    
    

