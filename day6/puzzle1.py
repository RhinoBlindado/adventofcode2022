# Double-Ended Queues
from collections import deque

"""
ADVENT OF CODE 2022

DAY 6 PUZZLE 1

"""

def hasRepeats(buffer):
    repeatedChars = True
    
    # A set cannot have repeated values, so if the list and set have the
    # same amount of items, there are not repeats in the buffer.
    if(len(buffer) == len(set(buffer))):
        repeatedChars = False
    
    return repeatedChars


#%% MAIN

# Load input
PATH = "input_sample.txt"
# PATH = "input.txt"

file = open(PATH, 'r')

# Load the single line to a variable.
datastream = file.readline()

#%%

# - Get the first four characters to the buffer, since there's no point in
# checking repeats before of it.
# - Start the counter a 4, the minimum possible.
buffer = deque(datastream[:4])
charsReceived = 4

# Loop over the rest of the datastream.
for char in datastream[4:]:
    
    # Check if has repeats, if not...
    if not hasRepeats(buffer):
        break
    else:
        # Pop the oldest received character, leftmost, and add the newest to the right.
        buffer.popleft()
        buffer.append(char)
        charsReceived += 1

print("The start-of-packet marker appears at {} characters processed.".format(charsReceived))

file.close()