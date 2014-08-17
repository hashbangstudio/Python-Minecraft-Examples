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

    # Get the current position that the player is located at in the world
    playerPosition = mc.player.getPos()

    # create the output message as a string
    message = "You are at ({0:.1f}, {1:.1f}, {2:.1f})".format(playerPosition.x, playerPosition.y, playerPosition.z)

    # print to the python interpreter standard output (terminal or IDLE probably)
    print(message)

    # send message to the minecraft chat
    mc.postToChat(message)
    #set default values
    newXposn = 0
    newZposn = 0
    numOfArgs = len(sys.argv)
    if numOfArgs == 3:
       # NOTE: This would be better handled in a try except for invalid input
       # Left out for clarity of example
       newXposn = float(sys.argv[1])
       newZposn = float(sys.argv[2])
    else:
        print("incorrect number of arguments")
        print("Usage: python script.py xCoord zCoord")
        print("Example usage: python script.py 9.2 8.5")
        sys.exit()

    newYposn = float(mc.getHeight(newXposn, newZposn))

    mc.player.setPos(newXposn, newYposn, newZposn)

    # Get the current position that the player is located at in the world
    playerPosition = mc.player.getPos()

    message = "You have been moved to ({0:.1f}, {1:.1f}, {2:.1f})".format(playerPosition.x, playerPosition.y, playerPosition.z)

    print(message)
    mc.postToChat(message)


