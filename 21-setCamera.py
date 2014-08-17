#!/usr/bin/env python

# We have to import the minecraft api module to do anything in the minecraft world
from mcpi.minecraft import *

import sys


def printAvailableCameraModes():
    print("Available camera modes are:")
    print("normal, follow, fixed")

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

    # remember this includes the name of the script as well
    minNumOfParams = 3
    numOfParamsGiven = len(sys.argv)

    if numOfParamsGiven >= minNumOfParams:
        cameraMode = sys.argv[1]

        if cameraMode == "follow" and sys.argv[2].isdigit() :
            mc.camera.setFollow(sys.argv[2])
        elif cameraMode == "normal" and sys.argv[2].isdigit():
            mc.camera.setNormal(sys.argv[2])
        elif cameraMode == "fixed":
            if numOfParamsGiven == 5 :
            #should verify arguments are integer coordinates
                mc.camera.setFixed()
                mc.camera.setPos(sys.argv[2], \
                                 sys.argv[3], \
                                 sys.argv[4])
            else:
                print("insufficient parameters given")
                print("Require 5 but got "+str(numOfParamsGiven))
        else:
            print("unknown camera mode parameter given "+ sys.argv[1])
            printAvailableCameraModes()
    else:
        print("insufficient parameters given")
        print("Require "+str(minNumOfParams)+", got "+str(numOfParamsGiven))
