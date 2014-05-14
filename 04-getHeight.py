# We have to import the minecraft api module to do anything in the minecraft world
from mcpi.minecraft import *

# this must be imported to get command line arguments
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

        x = playerPosition.x
        z = playerPosition.z

        numOfArgs = len(sys.argv) 

        if numOfArgs == 3:
            x = int(sys.argv[1]) 
            z = int(sys.argv[2])
        elif numOfArgs == 1:
            # just use the player position for x and z
            pass
        else:
            print("Expected 2 or 0 arguments but recieved "+str(numofArgs-1)) 
            print("To get the height of the world at the player")
            print("Usage: python script.py")
            print("To get the height of the world at a specific coordinate")
            print("Usage: python script.py x z")
    
        #get the height of the world at the coordinates (x,z)
        height = mc.getHeight(x, z)

    # create the output message as a string
    message = " height world is "+ str(height)+ " at "+ str((x,z))
    
    # print to the python interpreter standard output (terminal or IDLE probably)
    print(message)
    
    # send message to the minecraft chat
    mc.postToChat(message) 
 
