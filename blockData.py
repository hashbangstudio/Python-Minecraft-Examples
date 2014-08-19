#!/usr/bin/env python

# import block  definitions
from mcpi.block import *

BLOCK_ID_TO_NAME = {
AIR.id:"AIR",
STONE.id:"STONE",
GRASS.id:"GRASS",
DIRT.id:"DIRT",
COBBLESTONE.id:"COBBLESTONE",
WOOD_PLANKS.id:"WOOD_PLANKS",
SAPLING.id:"SAPLING",
BEDROCK.id:"BEDROCK",
WATER_FLOWING.id:"WATER_FLOWING",
WATER_STATIONARY.id:"WATER_STATIONARY",
LAVA_FLOWING.id:"LAVA_FLOWING",
LAVA_STATIONARY.id:"LAVA_STATIONARY",
SAND.id:"SAND",
GRAVEL.id:"GRAVEL",
GOLD_ORE.id:"GOLD_ORE",
IRON_ORE.id:"IRON_ORE",
COAL_ORE.id:"COAL_ORE",
WOOD.id:"WOOD",
LEAVES.id:"LEAVES",
GLASS.id:"GLASS",
LAPIS_LAZULI_ORE.id:"LAPIS_LAZULI_ORE",
LAPIS_LAZULI_BLOCK.id:"LAPIS_LAZULI_BLOCK",
SANDSTONE.id:"SANDSTONE",
BED.id:"BED",
COBWEB.id:"COBWEB",
GRASS_TALL.id:"GRASS_TALL",
WOOL.id:"WOOL",
FLOWER_YELLOW.id:"FLOWER_YELLOW",
FLOWER_CYAN.id:"FLOWER_CYAN",
MUSHROOM_BROWN.id:"MUSHROOM_BROWN",
MUSHROOM_RED.id:"MUSHROOM_RED",
GOLD_BLOCK.id:"GOLD_BLOCK",
IRON_BLOCK.id:"IRON_BLOCK",
STONE_SLAB_DOUBLE.id:"STONE_SLAB_DOUBLE",
STONE_SLAB.id:"STONE_SLAB",
BRICK_BLOCK.id:"BRICK_BLOCK",
TNT.id:"TNT",
BOOKSHELF.id:"BOOKSHELF",
MOSS_STONE.id:"MOSS_STONE",
OBSIDIAN.id:"OBSIDIAN",
TORCH.id:"TORCH",
FIRE.id:"FIRE",
STAIRS_WOOD.id:"STAIRS_WOOD",
CHEST.id:"CHEST",
DIAMOND_ORE.id:"DIAMOND_ORE",
DIAMOND_BLOCK.id:"DIAMOND_BLOCK",
CRAFTING_TABLE.id:"CRAFTING_TABLE",
FARMLAND.id:"FARMLAND",
FURNACE_INACTIVE.id:"FURNACE_INACTIVE",
FURNACE_ACTIVE.id:"FURNACE_ACTIVE",
DOOR_WOOD.id:"DOOR_WOOD",
LADDER.id:"LADDER",
STAIRS_COBBLESTONE.id:"STAIRS_COBBLESTONE",
DOOR_IRON.id:"DOOR_IRON",
REDSTONE_ORE.id:"REDSTONE_ORE",
SNOW.id:"SNOW",
ICE.id:"ICE",
SNOW_BLOCK.id:"SNOW_BLOCK",
CACTUS.id:"CACTUS",
CLAY.id:"CLAY",
SUGAR_CANE.id:"SUGAR_CANE",
FENCE.id:"FENCE",
GLOWSTONE_BLOCK.id:"GLOWSTONE_BLOCK",
BEDROCK_INVISIBLE.id:"BEDROCK_INVISIBLE",
STONE_BRICK.id:"STONE_BRICK",
GLASS_PANE.id:"GLASS_PANE",
MELON.id:"MELON",
FENCE_GATE.id:"FENCE_GATE",
GLOWING_OBSIDIAN.id:"GLOWING_OBSIDIAN",
NETHER_REACTOR_CORE.id:"NETHER_REACTOR_CORE"
}

def getBlockNameFromId(num):
    return blockIdToName[num]

#avaiable 0-1, affects whether striking blk sets off fuse
TNT_TYPE_NAME_TO_ID = {
"safe"  : 0,
"armed" : 1
}


#available range 0-15, affects colour of wool block
COLOUR_NAME_TO_ID = {
"white"      : 0,
"orange"     : 1,
"magenta"    : 2,
"light-blue" : 3,
"yellow"     : 4,
"lime"       : 5,
"pink"       : 6,
"grey"       : 7,
"gray"       : 7,
"light-grey" : 8,
"light-gray" : 8,
"cyan"       : 9,
"purple"     :10,
"blue"       :11,
"brown"      :12,
"green"      :13,
"red"        :14,
"black"      :15
}

# only 0-2 seem to do anything for texture
# 0 to 3 is type, beyond that is decay counter
# avilablerange 0-15 
LEAVES_TYPE_NAME_TO_ID = {
"oak"   : 0,
"pine"  : 1,
"spruce": 1,
"birch" : 2,
"jungle": 3
}


# only 0-2 seem to o anything
# available values 0-15 affects texture and rotation
WOOD_PLANKS_TYPE_NAME_TO_ID = {
"oak-up"       : 0,
"spruce-up"    : 1,
"birch-up"     : 2,
"jungle-up"    : 3,
"oak-east"     : 4,
"spruce-east"  : 5,
"birch-east"   : 6,
"jungle-east"  : 7,
"oak-north"    : 8,
"spruce-north" : 9,
"birch-north"  :10,
"jungle-north" :11,
"oak-bark"     :12,
"spruce-bark"  :13,
"birch-bark"   :14,
"jungle-bark"  :15
}

# available 0-15
# 6,7,14 and 15 don't work (uses default stone)
SLAB_TYPE_NAME_TO_ID = {
"stone"            : 0,
"sandstone"        : 1,
"wooden"           : 2,
"cobblestone"      : 3,
"brick"            : 4,
"stone-brick"      : 5,
#just is stone
"nether-brick"     : 6,
#just is stone
"quartz"           : 7,
"stone-top"        : 8,
"sandstone-top"    : 9,
"wooden-top"       :10,
"cobblestone-top"  :11,
"brick"            :12,
"stone-brick"      :13,
#just is stone
"nether-brick-top" :14,
#just is stone
"quartz-top"       :15,
}

#available 0-15
# only 1 to 5 does anything
# 6 and 7 wil use default stone
# above that just cycles back round 
DOUBLE_SLAB_TYPE_NAME_TO_ID = {
"stone"            : 0,
"sandstone"        : 1,
"wooden"           : 2,
"cobblestone"      : 3,
"brick"            : 4,
"stone-brick"      : 5,
#just is stone
"nether-brick"     : 6,

#just is stone
"quartz"           : 7
}

#available 0 to 2
SANDSTONE_TYPE_NAME_TO_ID = {
"sandstone" : 0,
"chiseled"  : 1,
"smooth"    : 2
}


# available 0 to 3
BED_TYPE_NAME_TO_ID = {
"south" : 0,
"west"  : 1,
"north" : 2,
"east"  : 3
}

# available 0 to 3
# no effect seemingly
GRASS_TYPE_NAME_TO_ID = {
"shub"        : 0,
"grass"       : 1,
"fern"        : 2,
"biome-shrub" : 3,
}

# there appears to be no difference for each value
YELLOW_FLOWER_TYPE_NAME_TO_ID = {
"yellow" : 0
}


# there appears to be no difference for each value
BLUE_FLOWER_TYPE_NAME_TO_ID = {
"blue" : 0
}

# direction of ascending 0 to 7 available
# 0 to 3 for normal stairs, 4-7 for inverted stairs
STAIRS_TYPE_NAME_TO_ID = {
"east" : 0,
"west" : 1,
"south": 2,
"north": 3,
"east-inverted" : 4,
"west-inverted" : 5,
"south-inverted": 6,
"north-inverted": 7
}

DOOR_TYPE_NAME_TO_ID = {
"northwest": 0,
"northeast": 1,
"southeast": 2,
"southwest": 3,
"northwest-swung": 0,
"northeast-swung": 1,
"southeast-swung": 2,
"southwest-swung": 3,
"northwest-top": 8,
"northeast-top": 9,
"southeast-top":10,
"southwest-top":11,
"northwest-top-swung":12,
"northeast-top-swung":13,
"southeast-top-swung":14,
"southwest-top-swung":15
}
