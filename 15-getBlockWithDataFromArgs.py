#!/usr/bin/env python

# We have to import the minecraft api module to do anything in the minecraft world
from mcpi.minecraft import *
from mcpi.block import *
from blockData import *
import sys
# this means that the file can be imported without executing anything in this code block
if __name__ == "__main__":

    """
    First thing you do is create a connection to minecraft
    This is like dialling a phone.
    It sets up a communication line between your script and the minecraft world
    """
    
    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()
    
    numOfArgs = len(sys.argv) - 1
    if numOfArgs == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
    elif numOfArgs == 2:
       x = int(sys.argv[1])
       z = int(sys.argv[2])
       #Get the block that would be stood on at this Horiz posn
       y = mc.getHeight(x,z) - 1
    else:
        print("Number of arguments incorrect")
        print("Expected 2 or 3 arguments but got %d" % (numOfArgs))
        print("Usage with 3 args: python script.py xcoord ycoord zcoord")
        print("Usage with 2 args: python script.py xcoord zcoord")
        sys.exit()
    
    blockAndData = mc.getBlockWithData(x, y ,z)
    blockName = getBlockNameFromId(blockAndData.id)
        
    # create message for the type of block
    message = "Block is of type " + str(blockAndData.id)+ " which is " + blockName
    # print to the python interpreter standard output (terminal or IDLE probably)
    print(message)
    # post message to the chat
    mc.postToChat(message) 

    message = "Block data " + str(blockAndData.data)
    # print to the python interpreter standard output (terminal or IDLE probably)
    print(message)
    # post message to the chat
    mc.postToChat(message) 

    if blockAndData.id == WOOL.id:
       print "is wool"
       for colour, colId in COLOUR_NAME_TO_ID.items():
           if colId == blockAndData.data:
               print "Colour is "+ colour

        

