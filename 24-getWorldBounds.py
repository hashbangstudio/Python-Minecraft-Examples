#!/usr/bin/env python

# We have to import the minecraft api module to do anything in the minecraft world
from mcpi.minecraft import *
from mcpi.block import *

def findWorldXLimits(mc):
    minX = 2560
    maxX = -2560
    x = 0
    z = 0
    while (True):
        
        height = mc.getHeight(x,z)
        # Get the type of block for the highest point in world at horiz player posn
        blockId = mc.getBlock(x, height , z)
        if(blockId == BEDROCK_INVISIBLE.id):
            #range() ends at one after last valid value so just use as is        
            maxX = x
            break
        # move to next block
        x += 1   
    
    x = 0 
    while (True):
        height = mc.getHeight(x,z)
        # Get the type of block for the highest point in world at horiz player posn
        blockId = mc.getBlock(x, height , z)
        
        if(blockId == BEDROCK_INVISIBLE.id):
           # range() starts at first valid value so add one
           minX =  x + 1
           break
        # move to next block
        x -=1
      
    return(minX, maxX)
   
def findWorldZLimits(mc):
    minZ = 2560
    maxZ = -2560
    x = 0
    z = 0                                                              
    while(True):
        height = mc.getHeight(x,z)
        # Get the type of block for the highest point in world at horiz player posn
        blockId = mc.getBlock(x, height , z)

        if (blockId == BEDROCK_INVISIBLE.id):
            #range() ends at one after last valid value so just use as is 
            maxZ = z
            break

        z += 1

    z = 0
    while(True):
        height = mc.getHeight(x,z)
        # Get the type of block for the highest point in world at horiz player posn
        blockId = mc.getBlock(x, height , z)

        if (blockId == BEDROCK_INVISIBLE.id):
            # range() starts at first valid value so add one
            minZ = z + 1
            break

        z -= 1
    return (minZ,maxZ)


# This means that the file can be imported without executing anything in this code block
if __name__ == "__main__":

    """
    First thing you do is create a connection to minecraft
    This is like dialling a phone.
    It sets up a communication line between your script and the minecraft world
    """
    
    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()

    xbounds = findWorldXLimits(mc)
    minX = xbounds[0]
    maxX = xbounds[1]
    print("x= ", minX, maxX)
    
    zbounds = findWorldZLimits(mc)
    minZ = zbounds[0]
    maxZ = zbounds[1]
 
    print("z= ", minZ, maxZ)
    
