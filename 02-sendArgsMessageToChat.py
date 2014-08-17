#!/usr/bin/env python

# We have to import the minecraft api module to do anything in the minecraft world
from mcpi.minecraft import *

# We have to import sys module to get the command line arguments
import sys

if __name__ == "__main__":

    """
    First thing you do is create a connection to minecraft
    This is like dialling a phone.
    It sets up a communication line between your script and the minecraft world
    """
    
    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()
    
    # Check that have the appropriate number of command line arguments (one in this case)
    # sys.argv is a list of the command line arguments given
    numOfArguments = len(sys.argv)
    if (numOfArguments == 2):
        # create the output message as a string
        message = sys.argv[1]
        # print to the python interpreter standard output (terminal or IDLE probably)
        print(message)
        # send message to the minecraft chat
        mc.postToChat(message) 
    else:
            # use -1 on num of arguments as first argument is the name of the script
        print("Expected only one string as argument for script, but received "+ str(numOfArguments - 1))

