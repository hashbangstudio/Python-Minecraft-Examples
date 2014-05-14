# We have to import the minecraft api module to do anything in the minecraft world
from mcpi.minecraft import *

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
    
        allIds = mc.getPlayerEntityIds()
    message = ""
        # create the output message as a string
    for id in allIds:
            message += "id is "+ str(id)
        # print to the python interpreter standard output (terminal or IDLE probably)
        print(message)
        # send message to the minecraft chat
        mc.postToChat(message) 
 
