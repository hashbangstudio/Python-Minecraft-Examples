#!/usr/bin/env python

# We have to import the minecraft api module to do anything in the minecraft world
from mcpi.minecraft import *

from random import randint

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
    message = " you are at (" +str(playerPosition.x)+","+str(playerPosition.y)+","+str(playerPosition.z)+")"

    # print to the python interpreter standard output (terminal or IDLE probably)
    print(message)

    # Send message to the minecraft chat
    mc.postToChat(message)

    # Randomly generates the amount to shift position by
    xShift = randint(-10, 10)
    zShift = randint(-10, 10)
    # Set variables for the new position
    newXposn = playerPosition.x + xShift
    newZposn = playerPosition.z + zShift
    # Set y position to be the height of the world so not in middle of a block
    newYposn = mc.getHeight(newXposn, newZposn)
    # Set the position of the player
    mc.player.setTilePos(newXposn, newYposn, newZposn)

    message = " you have been moved to (" +str(newXposn)+","+str(newYposn)+","+str(newZposn)+")"

    print(message)
    mc.postToChat(message)
