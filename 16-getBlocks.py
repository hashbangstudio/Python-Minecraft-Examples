# We have to import the minecraft api module to do anything in the minecraft world
from mcpi.minecraft import *
from mcpi.block import *


blockIdToName = {
0:"AIR",
1:"STONE",
2:"GRASS",
3:"DIRT",
4:"COBBLESTONE",
5:"WOOD_PLANKS",
6:"SAPLING",
7:"BEDROCK",
8:"WATER_FLOWING",
9:"WATER_STATIONARY",
10:"LAVA_FLOWING",
11:"LAVA_STATIONARY",
12:"SAND",
13:"GRAVEL",
14:"GOLD_ORE",
15:"IRON_ORE",
16:"COAL_ORE",
17:"WOOD",
18:"LEAVES",
20:"GLASS",
21:"LAPIS_LAZULI_ORE",
22:"LAPIS_LAZULI_BLOCK",
24:"SANDSTONE",
26:"BED",
30:"COBWEB",
31:"GRASS_TALL",
35:"WOOL",
37:"FLOWER_YELLOW",
38:"FLOWER_CYAN",
39:"MUSHROOM_BROWN",
40:"MUSHROOM_RED",
41:"GOLD_BLOCK",
42:"IRON_BLOCK",
43:"STONE_SLAB_DOUBLE",
44:"STONE_SLAB",
45:"BRICK_BLOCK",
46:"TNT",
47:"BOOKSHELF",
48:"MOSS_STONE",
49:"OBSIDIAN",
50:"TORCH",
51:"FIRE",
53:"STAIRS_WOOD",
54:"CHEST",
56:"DIAMOND_ORE",
57:"DIAMOND_BLOCK",
58:"CRAFTING_TABLE",
60:"FARMLAND",
61:"FURNACE_INACTIVE",
62:"FURNACE_ACTIVE",
64:"DOOR_WOOD",
65:"LADDER",
67:"STAIRS_COBBLESTONE",
71:"DOOR_IRON",
73:"REDSTONE_ORE",
78:"SNOW",
79:"ICE",
80:"SNOW_BLOCK",
81:"CACTUS",
82:"CLAY",
83:"SUGAR_CANE",
85:"FENCE",
89:"GLOWSTONE_BLOCK",
95:"BEDROCK_INVISIBLE",
98:"STONE_BRICK",
102:"GLASS_PANE",
103:"MELON",
107:"FENCE_GATE",
246:"GLOWING_OBSIDIAN",
247:"NETHER_REACTOR_CORE"
}

def getBlockNameFromId(num):
    return blockIdToName[num]


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
	
        height = mc.getHeight(playerPosition.x, playerPosition.z)
	# create the output message as a string
	message = " height is "+ str(height)

        # Get the type of block for the highest point in world at horiz player posn
        # Need to do height minus one for this
        blocksInCuboid = mc.getBlocks(playerPosition.x, height, playerPosition.z, \
                                  playerPosition.x + 10, height, playerPosition.z + 10)

        print(blocksInCuboid) 
        
        # Add to message, the type of block stood on
#	message += "\n Block is of type " + str(blockIdNum)+ " which is " + getBlockNameFromId(blockIdNum)

    	# print to the python interpreter standard output (terminal or IDLE probably)
	print(message)

        # send message to the minecraft chat
	mc.postToChat(message) 
