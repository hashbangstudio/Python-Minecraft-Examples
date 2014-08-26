#!/usr/bin/env python

# We have to import the minecraft api module to do anything in the minecraft world
from mcpi.minecraft import *

import sys


def printAvailableCameraModes():
    print("Available camera modes are:")
    print("normal, follow, fixed")

def printUsage():
    print("Usage : python script.py normal [entityId]")
    print("Usage : python script.py follow [entityId]")
    print("Usage : python script.py fixed Xcoord Ycoord Zcoord")

    
    

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

    minNumOfParams = 1
    # Remember that this also includes the script name
    numOfParamsGiven = len(sys.argv) - 1

    if numOfParamsGiven >= minNumOfParams:
        cameraMode = sys.argv[1]

        if cameraMode == "follow" :
            if numOfParamsGiven == 1:
                mc.camera.setFollow()
            elif numOfParamsGiven == 2 and sys.argv[2].isdigit():
                mc.camera.setFollow(sys.argv[2])
            else:
               print("Expected 1 or 2 parameters but got "+str(numOfParamsGiven))
               printUsage()
               exit()
        elif cameraMode == "normal" :
            if numOfParamsGiven == 1:
                mc.camera.setNormal()
            elif numOfParamsGiven == 2 and sys.argv[2].isdigit():
                mc.camera.setNormal(sys.argv[2])
            else:
               print("Expected 1 or 2 parameters but got "+str(numOfParamsGiven))
               printUsage()
               exit()
        elif cameraMode == "fixed":
            if numOfParamsGiven == 4 :
            #should verify arguments are integer coordinates
                mc.camera.setFixed()
                mc.camera.setPos(sys.argv[2], \
                                 sys.argv[3], \
                                 sys.argv[4])
            else:
                print("insufficient parameters given")
                print("Require 4 but got "+str(numOfParamsGiven))
                printUsage()
                exit()
        else:
            print("unknown camera mode parameter given "+ sys.argv[1])
            printAvailableCameraModes()
            printUsage()
            exit()
    else:
        print("insufficient parameters given")
        print("Require minimum of "+str(minNumOfParams)+", got "+str(numOfParamsGiven))
        printUsage()
        exit()
