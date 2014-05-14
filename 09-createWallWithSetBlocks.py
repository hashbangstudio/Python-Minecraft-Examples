#import the needed modules
from mcpi.minecraft import *
from mcpi.block import *
from time import sleep

if __name__ == "__main__":

    # Create a connection to the Minecraft game
    mc = Minecraft.create()
    
    # Get the player position
    playerPosition = mc.player.getTilePos()

        wallStartXposn = playerPosition.x + 6
        wallStartYposn = playerPosition.y + 1
        wallZposn = playerPosition.z + 6

        wallEndXposn = wallStartXposn + 10
        wallEndYposn = wallStartYposn + 6

        # Create a wall
        mc.setBlocks(wallStartXposn , wallStartYposn, wallZposn,\
                     wallEndXposn,    wallEndYposn,   wallZposn, \
                     DIAMOND_BLOCK)
