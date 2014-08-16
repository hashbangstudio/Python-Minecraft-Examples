#import the needed modules fo communication with minecraft world
from mcpi.minecraft import *
from mcpi.block import *
if __name__ == "__main__":

    # Create a connection to the Minecraft game
    mc = Minecraft.create()

    # Get the player position
    playerPosition = mc.player.getTilePos()

    # define the position of the block
    blockXposn = playerPosition.x + 1
    blockYposn = playerPosition.y + 1
    blockZposn = playerPosition.z + 1

    print("Creating block at", blockXposn, blockYposn, blockZposn)
    # Create a block
    mc.setBlock(blockXposn, blockYposn, blockZposn, DIAMOND_BLOCK)
