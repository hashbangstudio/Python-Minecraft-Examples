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
    
    # get the output message as a string from keyboard input
    # NOTE this is python 2, in Python 3 input() should be used
    message = raw_input("Please enter some text to send to the chat: ")
    # print to the python interpreter standard output (terminal or IDLE probably)
    print(message)
    # send message to the minecraft chat
    mc.postToChat(message) 

