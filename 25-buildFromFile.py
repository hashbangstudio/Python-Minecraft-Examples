# We have to import the minecraft api module to do anything in the minecraft world
from mcpi.minecraft import *
from mcpi.block import *
# We have to import sys module to get the command line arguments
import sys


if __name__ == "__main__":


    """
    First thing you do is create a connection to minecraft
    This is like dialling a phone.
    It sets up a communication line between your script and the minecraft world
    """
    
    # Create a connection to Minecraft
    # Any communication with the world must use this object
    mc = Minecraft.create()
    
    # Check that have the appropriate number of command line arguments (one in this case)
    # sys.argv is a list of the command line arguments given
    numOfArguments = len(sys.argv)
    if (numOfArguments == 2):
        # get the name of the file to open
        filenameToOpen = sys.argv[1]
        # print to the python interpreter standard output (terminal or IDLE probably)
        print ("Opening " + filenameToOpen+'\n')
    
        """
        Open the file
        Read through the file line by line 
        This uses a try catch statement when opening the file
        The code will only send to chat if the file is opened and read successfully
        If an error (Exception) occurs it is printed out to the console
        """
        try:
            # this opup the text file in read only ('r') mode
            textFile = open(filenameToOpen, mode='r')
            numOfLines = 0
            # go through the text file line by line
            for line in textFile:
                numOfLines +=1
            
            print("there are "+ str(numOfLines) +" lines in the textFile")
            block = AIR
            playerPos = mc.player.getTilePos()
            startX = playerPos.x - 16
            x = startX
            y = playerPos.y + 1 + numOfLines
            z = playerPos.z - 16
            
            currentLine = 1
            textFile.seek(0) 
            for line in textFile:
                print ("building line "+ str(currentLine)+ " of "+ str(numOfLines))
                x = startX
                for character in line:
                    x += 1
                    print("character is " + character)
                    if character in ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']:
                        colour = int(character,16)
                        print("colour = "+ str(colour))
                        if colour in range(16): 
                            block = WOOL.withData(colour)
                        else:
                            block = WOOL
                    else:
                        block = AIR
                    print("setting block "+ str(block)+" at "+str( (x,y,z)))
                    mc.setBlock(x, y, z, block)    
                y -= 1
                currentLine += 1 
        except IOError as e:
            print("Failed to open file")
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
        finally:
            textFile.close()

    else:
        # use num of arguments -1 as first argument is the name of this script
        print("Expected only one filename as argument, but received "+ str(numOfArguments-1))
