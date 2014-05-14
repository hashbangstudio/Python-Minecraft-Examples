#import the needed modules
from mcpi.minecraft import *
from mcpi.block import *

if __name__ == "__main__":

    # Create a connection to the Minecraft game
    mc = Minecraft.create()
    
    # Get the player position
    playerPosition = mc.player.getTilePos()
    
    # Set coordinates (position) for the block that is slightly away from the player
    # Note y is the vertical coordinate, x and z the horizontal
    blockYposn = playerPosition.y+1
    blockZposn = playerPosition.z+1
    
    for column in range(16):
        #increase the distance along and up that the block is placed at
        blockXposn = playerPosition.x + 1 + column
        print("Creating block at", blockXposn, blockYposn)
        # Create a block
        mc.setBlock(blockXposn, blockYposn, blockZposn, WOOL.withData(column))
    
