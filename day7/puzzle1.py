# Double-Ended Queues
from collections import deque

"""
ADVENT OF CODE 2022

DAY 7 PUZZLE 1

"""

class TreeNode:
    """
    Class to hold each directory node.
    """
    
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.parent = None
        self.children = []
        
    def addChild(self, child):
        self.children.append(child)
        child.setParent(self)
    
    def getChild(self, name):
        for chld in self.children:
            if(chld.name == name):
                return chld
    
        return None
        
    def getChildren(self):
        return self.children
    
    def getSize(self):
        return self.size
    
    def addSize(self, size):
        self.size += size
    
    def getParent(self):
        return self.parent
    
    def setParent(self, node):
        self.parent = node
        
    def __repr__(self):
        output = "{}".format(self.name)
        return output
    
class Tree:
    def __init__(self, node):
        self.root = node
        self.actDir = node
        
    def __repr__(self):
        output = "Actual dir: {} | Size: {} | Parent: {} | Children: {}".format(self.actDir.name, self.actDir.size, self.actDir.parent, self.actDir.getChildren())
        return output
    
    def goUpTree(self):
        self.actDir = self.actDir.getParent()
        
    def addFolder(self, node):
        self.actDir.addChild(node)
        
    def goDownTree(self, name):
        self.actDir = self.actDir.getChild(name)
        
    def getActualDir(self):
        return self.actDir
    
    def addSize(self, size):
        self.actDir.addSize(size) 
        
        parent = self.actDir.getParent()
        
        while(parent is not None):
            parent.addSize(size)
            parent = parent.getParent()

    def resetToRoot(self):
        self.actDir = self.root
        
    def calculateTotalSize(self, limit):
        # Go to root and start the recursion...
        actNode = self.root
        totalSum = 0
        
        return totalSumRecursion(actNode, totalSum, limit)


def totalSumRecursion(node, total, valMax):
    
        # Travel each child exactly once.
        children = node.getChildren()
        
        while(len(children) > 0):
            total = totalSumRecursion(children.pop(), total, valMax)
        
        # After traveling all children or getting to a leaf node, sum the size if it's 
        # below the limit and return the added value.
        if(node.getSize() <= valMax):
            # print("Directory {} has {}".format(node.name, node.size))
            total += node.getSize()  
        
        return total

     
def parse(line, dirTree):
    
    # Ignore if line is "ls", since it doesn't do anything here.
    if(line[1] == "cd"):       
        # If ".." is present, it means go up one folder. Change the pointer.
        if(line[2] == ".."):
            dirTree.goUpTree()
        else:
        # Go down the specified folder, changes the pointer.
            dirTree.goDownTree(line[2])

#%% MAIN
# Load input
# PATH = "input_sample.txt"
PATH = "input.txt"

file = open(PATH, 'r')

# Ignore the first two lines.
_ = file.readline()
_ = file.readline()

#%%

# Create the root of the filesystem
dirTree = Tree(TreeNode("/"))

for line in file:
   
    # Get each line as strings in a vector.
    line = line.split()

    # If starts with "$", it's command. Parse it.
    if(line[0] == "$"):
        parse(line, dirTree)
    else:
    # If not, check if it's a directory, add it to the current directory children.
        if(line[0] == "dir"):
            tmpNode = TreeNode(line[1])
            dirTree.addFolder(tmpNode)
        else:
        # If not, it's a file. Add its size to the current directory size.
        # - Size is added to the parent folders up to the root.
            dirTree.addSize(int(line[0]))

# Calculate the total sum.
totalSum = dirTree.calculateTotalSize(100000)

print("The total sum of bytes of directories with <=  100000 is {}".format(totalSum))

file.close()