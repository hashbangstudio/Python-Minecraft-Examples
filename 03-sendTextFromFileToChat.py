# We have to import the minecraft api module to do anything in the minecraft world
from mcpi.minecraft import *

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
        Read through the file line by line and post it to the chat
        This uses a try catch statement when opening the file
        The code will only send to chat if the file is opened and read successfully
        If an error (Exception) occurs it is printed out to the console
        """
        try:
            # this opens up the text file in read only ('r') mode
            textFile = open(filenameToOpen, mode='r')
            # Each line in the text file must be sent as a separate message

            # go through the text file line by line
            for line in textFile:
                # send message to the minecraft chat
                mc.postToChat(line)
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
