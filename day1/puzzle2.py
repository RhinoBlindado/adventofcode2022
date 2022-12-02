import argparse 
import sys
import numpy as np

parser = argparse.ArgumentParser("Advent of Code Day 1 Puzzle 2")
parser.add_argument('--path', required=True, help='Path to data.')


sys.argv = ['puzzle2.py', '--path', "./input.txt"]

args = parser.parse_args()

file = open(args.path, 'r')


elves = []
actSum = 0

for line in file:

    if(line == "\n"):
        elves.append(actSum)

        actSum = 0
        
    else:
        actSum += int(line)


sortedElves = np.sort(elves)[::-1]

topThreeCals = np.sum(sortedElves[0:3])

print("The top three Elves have {} total calories.".format(topThreeCals))