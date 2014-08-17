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
    
    numOfArgs = len(sys.argv)
    if numOfArgs == 4:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3]) 
    else:
        print("Number of arguments incorrect")
        sys.exit()
    
    # Get the type of block for the highest point in world at horiz player posn
    blockAndData = mc.getBlockWithData(x, y ,z)
        
    if blockAndData.id == AIR.id:
        # Need to do height minus one for this
        blockAndData = mc.getBlockWithData(x, y -1 , z)
    blockName = getBlockNameFromId(blockAndData.id)
        
    # Add to message, the type of block stood on
    message = "  Block is of type " + str(blockAndData.id)+ " which is " + blockName
    # print to the python interpreter standard output (terminal or IDLE probably)
    print(message)
    # post message to the chat
    mc.postToChat(message) 

    if blockAndData.id == WOOL.id:
       print "is wool"
       for colour, colId in woolColourNameToId.items():
           if colId == blockAndData.data:
               print "Colour is "+ colour

        

