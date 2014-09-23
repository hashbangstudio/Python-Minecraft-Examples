Python-Minecraft-Examples
=========================

A set of examples of how to use the Minecraft Python API and Minecraft Pi edition

To use these examples first you need to have Minecraft installed:

If you have a recently updated version of Raspbian you can install Minecraft-Pi from the repositories.

1. Open LXTerminal by double clicking on the icon on the desktop or click on :
  Start Menu > Accessories > LXTerminal
2. Type the following commands and press enter after each one:
  * `sudo apt-get update`
  * `sudo apt-get install minecraft-pi`
3. You should now see a minecraft shortcut icon on the desktop. Double click on this to start minecraft pi

Alternatively you can start minecraft from the terminal:

1. Open LXTerminal by double clicking on the icon on the desktop or click on :
  Start Menu > Accessories > LXTerminal
2. type `minecraft-pi` and press enter. Note if you wish to start minecraft in the background you need to type `minecraft-pi &`


If you have an older version of Raspbian you need to do the following:

1. Go to http://pi.minecraft.net
2. Click on *Downloads* in the menu bar
3. Click on the download link
  * As of 15th May 2014 the link was:
  * https://s3.amazonaws.com/assets.minecraft.net/pi/minecraft-pi-0.1.1.tar.gz

4. Unzip/Uncompress this file by navigating to it in the *File Manager* and right clicking on it and click on *Extract here*
5. Go into the newly created folder *mcpi*
6. Double click on the file *minecraft-pi* and choose *Execute*
7. This will have opened up Minecraft, you need to start a game and create a new world

Now that Minecraft is running and you are in the world you can run the examples.
All examples can be run from the command line in LXTerminal. 
To run in IDLE some examples need slight modification first to replace the usage of command line arguments

##Running the Examples in LXTerminal

1. Open LXTerminal by double clicking on the icon on the desktop or click on :
  Start Menu > Accessories > LXTerminal

2. Navigate to the folder where these examples are, assuming you have uncompressed the zip folder or cloned the repository in your home folder :
 `cd Python-Minecraft-Examples`
3. Type: `python filename.py` and press enter (where filename is the examples to try)
4. Where the script expects arguments you supply those after the filename. or example:
   `python 02-sendArgsMessageToChat.py "This is a message"`
5. Have fun in Minecraft! 


##Running the Examples in IDLE

1. Open IDLE by double clicking on the icon on the desktop or open LXTerminal and type `idle &` and press enter
2. Go to : File > Open 
3. Open an example file
4. Press F5 or in the Menu go to  Run > Run Module

Note: for those  examples that require command line arguments this is easily worked around.
For example with file *02-sendArgsMessageToChat.py* we edit the file so that below the line that reads :
```python
if __name__ == '__main__':
```
We add the following line so it becomes:
```python
if __name__ == '__main__':
    sys.argv = [sys.argv[0], "this is a message"]
```
NOTE : the new line should begin with 4 spaces for correct indentation

In general you can add any number of arguments this way
```python
if __name__ == '__main__':
    sys.argv = [sys.argv[0], argument1, argument2, argument3]
```
