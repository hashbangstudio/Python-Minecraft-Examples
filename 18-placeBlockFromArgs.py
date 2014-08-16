#import the needed modules
from mcpi.minecraft import *
from mcpi.block import *
import sys

if __name__ == "__main__":

    # Create a connection to the Minecraft game
    mc = Minecraft.create()

    # Get the player position
    playerPosition = mc.player.getTilePos()

    # Set coordinates (position) for the block that is slightly away from the player
    # Note y is the vertical coordinate, x and z the horizontal
    blockXposn = playerPosition.x + 1
    blockZposn = playerPosition.z + 1
    # set the y coordinate to be at the height of the world at the (x,z) horisontal coordinate
    blockYposn = mc.getHeight(blockXposn, blockZposn)
    blockToPlace = AIR
    numOfArgs = len(sys.argv)
    if numOfArgs == 2 or numOfArgs == 3 :
        blockArgs = sys.argv[1].replace('(','').replace(')','').split(',')
        blockId = int(blockArgs[0])
        blockData = int(blockArgs[1])

        blockToPlace = Block(blockId,blockData)
        if numOfArgs == 3:
            coords = sys.argv[2].replace('(','').replace(')','').split(',')
            print ("using coords = " + str(coords))
            blockXposn = int(coords[0])
            blockYposn = int(coords[1])
            blockZposn = int(coords[2])
    else:
        print("To place block next to player:")
        print("Usage : python script.py blockId,blockData")
        print("To place block at a specific coordinate")
        print("Usage : python script.py blockId,blockData x,y,z")
        print("Expected 1 or 2 aguments but received " + str(numOfArgs-1))
        sys.exit()

    print str(blockToPlace)
    print str((blockXposn, blockYposn, blockZposn))

    mc.setBlock(blockXposn, blockYposn, blockZposn, blockToPlace)

