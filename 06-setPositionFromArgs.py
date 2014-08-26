#!/usr/bin/env python

# We have to import the minecraft api module to do anything in the minecraft world
from mcpi.minecraft import *

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

    # Get the current tile/block that the player is located at in the world
    playerPosition = mc.player.getTilePos()

    # create the output message as a string
    message = "You are at (" +str(playerPosition.x)+","+str(playerPosition.y)+","+str(playerPosition.z)+")"

    # print to the python interpreter standard output (terminal or IDLE probably)
    print(message)

    # send message to the minecraft chat
    mc.postToChat(message)
    #Set Default values
    newXposn = 0
    newZposn = 0
    numOfArgs = len(sys.argv)
    if numOfArgs == 3:
        # Use float first in case argument is 3.3 string to avoid value error
        newXposn = int(float(sys.argv[1]))
        newZposn = int(float(sys.argv[2]))
    else:
        print("incorrect number of arguments")
        sys.exit()

    newYposn = mc.getHeight(newXposn, newZposn)

    mc.player.setTilePos(newXposn, newYposn, newZposn)

    # Get the current tile/block that the player is located at in the world
    playerPosition = mc.player.getTilePos()

    message = "You are now at (" +str(playerPosition.x)+","+str(playerPosition.y)+","+str(playerPosition.z)+")"

    print(message)
    mc.postToChat(message)


