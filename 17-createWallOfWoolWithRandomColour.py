#import the needed modules fo communication with minecraft world
from mcpi.minecraft import *
# import needed block defintiions
from mcpi.block import *
# needed to slow down the wall building
from time import sleep
# needed to generate a random number for the colour of wool
from random import randint

if __name__ == "__main__":

    # Create a connection to the Minecraft game
    mc = Minecraft.create()
    
    # Get the player position
    playerPosition = mc.player.getTilePos()
    
        # define the position of the bottom left block of the wall
        blockXposn = playerPosition.x + 6
        firstColumnX = blockXposn 
        blockYposn = playerPosition.y + 1
        blockZposn = playerPosition.z + 6

    # Create a wall using nested for loops
    for row in range(6):
            # increase the height of th current row to be built
            blockYposn += 1
            blockXposn = firstColumnX
        for column in range(10):
            #increase the distance along the row that the block is placed at
            blockXposn += 1
                #Generate a random number within the allowed range of colours
                randomNumber = randint(0,15)
                print("random number to be used = "+ str(randomNumber))
            print("Creating block at", blockXposn, blockYposn)
            # Create a block
            mc.setBlock(blockXposn, blockYposn, blockZposn, WOOL.withData(randomNumber))
                sleep(0.5)
