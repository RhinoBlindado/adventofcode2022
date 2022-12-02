import argparse 

parser = argparse.ArgumentParser("Advent of Code Day 1 Puzzle 1")
parser.add_argument('--path', required=True, help='Path to data.')

args = parser.parse_args()

file = open(args.path, 'r')

maxSum = -1
actSum = 0

for line in file:

    if(line == "\n"):
        if(actSum > maxSum):
            maxSum = actSum

        actSum = 0
        
    else:
        actSum += int(line)

print("Max calories are: {}".format(maxSum))