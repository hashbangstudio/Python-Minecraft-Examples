import mcpi.minecraft as minecraft
import mcpi.block as block



def createLowerCaseLetterA(minecraftConnection, lowerLeftX, lowerLeftY, lowerLeftZ, blockType, blockData):
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY, lowerLeftZ+1,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY, lowerLeftZ+2,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY, lowerLeftZ+3,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY, lowerLeftZ+4,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY+1, lowerLeftZ+1,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY+1, lowerLeftZ+4,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY+2, lowerLeftZ+1,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY+2, lowerLeftZ+4,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY+3, lowerLeftZ+1,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY+3, lowerLeftZ+2,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY+3, lowerLeftZ+3,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY+3, lowerLeftZ+4,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY+4, lowerLeftZ+4,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY+5, lowerLeftZ+1,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY+5, lowerLeftZ+4,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY+6, lowerLeftZ+1,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY+6, lowerLeftZ+2,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY+6, lowerLeftZ+3,blockType.withData(blockData))
    minecraftConnection.setBlock(lowerLeftX+1, lowerLeftY+6, lowerLeftZ+4,blockType.withData(blockData)) 
    

if __name__ == "__main__":
    
    mc = minecraft.Minecraft.create()
    pos = mc.player.getTilePos()
    print(" you are at (" +str(pos.x)+","+str(pos.y)+","+str(pos.z)+")") 
    mc.postToChat(" you are at (" +str(pos.x)+","+str(pos.y)+","+str(pos.z)+")") 
    createLowerCaseLetterA(mc, pos.x, pos.y, pos.z, block.WOOL, 3)

