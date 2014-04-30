import mcpi.minecraft as minecraft
import mcpi.block as mc_block
import sys

A = [" 111 ",
     "1   1",
     "1   1"
     "11111",
     "11111",
     "1   1",
     "1   1"]


B = ["1111 ",
     "1   1",
     "1   1",
     "1111 ",
     "1   1",
     "1   1",
     "1111 "]


C = [" 111 ",
     "1   1",
     "1    ",
     "1    ",
     "1    ",
     "1   1",
     " 111 "]

D = ["111  ",
     "1  1 ",
     "1   1",
     "1   1",
     "1   1",
     "1  1 ",
     "111  "]

E = ["11111",
     "1    ",
     "1    ",
     "11111",
     "1    ",
     "1    ",
     "11111"]

F = ["11111",
     "1    ",
     "1    ",
     "11111",
     "1    ",
     "1    ",
     "1    "]

G = [" 111 ",
     "1   1",
     "1    ",
     "1    ",
     "1 111",
     "1   1",
     " 111 "]

H = ["1   1",
     "1   1",
     "1   1",
     "11111",
     "1   1",
     "1   1",
     "1   1"]

I = ["11111",
     "  1  ",
     "  1  ",
     "  1  ",
     "  1  ",
     "  1  ",
     "11111"]

J = ["11111",
     "  1  ",
     "  1  ",
     "  1  ",
     "1 1  ",
     "1 1  ",
     "111  "]

K = ["1   1",
     "1  1 ",
     "1 1  ",
     "11   ",
     "1 1  ",
     "1  1 ",
     "1   1"]

L = ["1    ",
     "1    ",
     "1    ",
     "1    ",
     "1    ",
     "1    ",
     "11111"]

M = ["1   1",
     "11 11",
     "1 1 1",
     "1   1",
     "1   1",
     "1   1",
     "1   1"]

N = ["1   1",
     "11  1",
     "1 1 1",
     "1  11",
     "1   1",
     "1   1",
     "1   1"]

O = [" 111 ",
     "1   1",
     "1   1",
     "1   1",
     "1   1",
     "1   1",
     " 111 "]

P = ["1111 ",
     "1   1",
     "1   1",
     "1111 ",
     "1    ",
     "1    ",
     "1    "]

Q = [" 11  ",
     "1  1 ",
     "1  1 ",
     "1  1 ",
     "1  1 ",
     "1  1 ",
     " 1111"]

R = ["1111 ",
     "1   1",
     "1   1",
     "1111 ",
     "1 1  ",
     "1  1 ",
     "1   1"]

S = [" 111 ",
     "1   1",
     "1    ",
     " 111 ",
     "    1",
     "1   1",
     " 111 "]

T = ["11111",
     "  1  ",
     "  1  ",
     "  1  ",
     "  1  ",
     "  1  ",
     "  1  "]

U = ["1   1",
     "1   1",
     "1   1",
     "1   1",
     "1   1",
     "1   1",
     " 111 "]

V = ["1   1",
     "1   1",
     "1   1",
     "1   1",
     "1   1",
     " 1 1 ",
     "  1  "]

W = ["1   1",
     "1   1",
     "1   1",
     "1   1",
     "1 1 1",
     "11 11",
     "1   1"]

X = ["1   1",
     "1   1",
     " 1 1 ",
     "  1  ",
     " 1 1 ",
     "1   1",
     "1   1"]

Y = ["1   1",
     "1   1",
     " 1 1 ",
     "  1  ",
     "  1  ",
     "  1  ",
     "  1  "]

Z = ["11111",
     "    1",
     "   1 ",
     "  1  ",
     " 1   ",
     "1    ",
     "11111"]

a = ["     ",
     "     ",
     " 11  ",
     "   1 ",
     "1111 ",
     "1  1 ",
     "1111 "]


b = ["     ",
     "     ",
     "1    ",
     "1    ",
     "1111 ",
     "1  1 ",
     "1111 "]


c = ["     ",
     "     ",
     " 11  ",
     "1  1 ",
     "1    ",
     "1  1 ",
     " 11  "]

d = ["     ",
     "     ",
     "   1 ",
     "   1 ",
     " 111 ",
     "1  1 ",
     " 1111"]

e = ["     ",
     "     ",
     " 111 ",
     "1   1",
     "1111 ",
     "1    ",
     " 1111"]

f = ["     ",
     "     ",
     " 11  ",
     "1  1 ",
     "11   ",
     "1    ",
     "1    "]

g = ["     ",
     "     ",
     " 111 ",
     "1  1 ",
     " 111 ",
     "   1 ",
     "111  "]

h = ["     ",
     "     ",
     "1    ",
     "1    ",
     "1111 ",
     "1  1 ",
     "1  1 "]

i = ["     ",
     "     ",
     "  1  ",
     "     ",
     "  1  ",
     "  1  ",
     "  1  "]

j = ["     ",
     "     ",
     "   1 ",
     "     ",
     "   1 ",
     "1  1 ",
     " 11  "]

k = ["     ",
     "     ",
     "1    ",
     "1 1  ",
     "11   ",
     "1 1  ",
     "1  1 "]

l = ["     ",
     "     ",
     "1    ",
     "1    ",
     "1    ",
     "1  1 ",
     " 11  "]

m = ["     ",
     "     ",
     " 111 ",
     "1 1 1",
     "1 1 1",
     "1   1",
     "1   1"]

n = ["     ",
     "     ",
     " 111 ",
     "1   1",
     "1   1",
     "1   1",
     "1   1"]

o = ["     ",
     "     ",
     " 111 ",
     "1   1",
     "1   1",
     "1   1",
     " 111 "]

p = ["     ",
     "     ",
     "111  ",
     "1  1 ",
     "111  ",
     "1    ",
     "1    "]

q = ["     ",
     "     ",
     " 111 ",
     "1  1 ",
     " 111 ",
     "   1 ",
     "   11"]

r = ["     ",
     "     ",
     " 11  ",
     "1  1 ",
     "1    ",
     "1    ",
     "1    "]

s = ["     ",
     "     ",
     " 111 ",
     "1    ",
     " 11  ",
     "   1 ",
     "111  "]

t = ["     ",
     "     ",
     " 1   ",
     "111  ",
     " 1   ",
     " 1 1 ",
     " 111 "]

u = ["     ",
     "     ",
     "1   1",
     "1   1",
     "1   1",
     "1   1",
     " 111 "]

v = ["     ",
     "     ",
     "1   1",
     "1   1",
     "1   1",
     " 1 1 ",
     "  1  "]

w = ["     ",
     "     ",
     "1   1",
     "1   1",
     "1 1 1",
     "11 11",
     "1   1"]

x = ["     ",
     "     ",
     "1   1",
     " 1 1 ",
     "  1  ",
     " 1 1 ",
     "1   1"]

y = ["     ",
     "     ",
     "1  1 ",
     "1  1 ",
     " 111 ",
     "   1 ",
     "111  "]

z = ["     ",
     "     ",
     "11111",
     "   1 ",
     "  1  ",
     " 1   ",
     "11111"]

ONE_1 = ["  1  ",
         " 11  ",
         "1 1  ",
         "  1  ",
         "  1  ",
         "  1  ",
         "11111"]

TWO_2 = ["11111",
        "    1",
        "    1",
        "11111",
        "1    ",
        "1    ",
        "11111"]

THREE_3 = [" 111 ",
           "1   1",
           "    1",
           " 111 ",
           "    1",
           "1   1",
           " 111 "]

FOUR_4 = ["1   1",
          "1   1",
          "1   1",
          "11111",
          "    1",
          "    1",
          "    1"]

FIVE_5 = ["11111",
          "1    ",
          "1    ",
          "11111",
          "    1",
          "    1",
          "11111"]

SIX_6 = ["1111 ",
         "1    ",
         "1    ",
         "11111",
         "1   1",
         "1   1",
         "11111"]

SEVEN_7 = ["11111",
           "    1",
           "   1 ",
           "  1  ",
           " 1   ",
           " 1   ",
           " 1   "]

EIGHT_8 = ["11111",
           "1   1",
           "1   1",
           "11111",
           "1   1",
           "1   1",
           "11111"]

NINE_9 = [" 111 ",
          "1   1",
          "1   1",
          " 111 ",
          "   1 ",
          "  1  ",
          " 1   "]


ZERO_0  = [" 111 ",
          "1   1",
          "1  11",
          "1 1 1",
          "11  1",
          "1   1",
          " 111 "]

BRACKET_OPEN = ["  1  ",
                " 1   ",
                "1    ",
                "1    ",
                "1    ",
                " 1   ",
                "  1  "]

BRACKET_CLOSE = ["  1  ",
                 "   1 ",
                 "    1",
                 "    1",
                 "    1",
                 "   1 ",
                 "  1  "]


FORWARD_SLASH = ["     ",
                 "    1",
                 "   1 ",
                 "  1  ",
                 " 1   ",
                 "1    ",
                 "     "]

DIVIDE = ["     ",
          "  1  ",
          "     ",
          "11111",
          "     ",
          "  1  ",
          "     "]

DOT = ["     ",
       "     ",
       " 111 ",
       " 111 ",
       " 111 ",
       "     ",
       "     "]

PLUS = ["  1  ",
        "  1  ",
        "  1  ",
        "11111",
        "  1  ",
        "  1  ",
        "  1  "]

MINUS = ["     ",
         "     ",
         "     ",
         "11111",
         "     ",
         "     ",
         "     "]

DOLLAR_US = ["  1  ",
             " 1111",
             "1 1  ",
             " 111 ",
             "  1 1",
             "1111 ",
             "  1  "]

POUND_STERLING = ["  1  ",
                  " 1 1 ",
                  " 1   ",
                  "111  ",
                  " 1   ",
                  " 1   ",
                  "1111 "]

CARET = ["  1  ",
         " 1 1 ",
         "1   1",
         "     ",
         "     ",
         "     ",
         "     "]

ASTERIX = ["  1  ",
           "1 1 1",
           " 111 ",
           "11111",
           " 111 ",
           "1 1 1",
           "  1  "]

AMPERSAND = [" 1   ",
             "1 1  ",
             "1 1  ",
             " 1   ",
             "1 1 1",
             "1  1 ",
             " 11 1"]

EXCLAMATION_MARK = ["  1  ",
                    "  1  ",
                    "  1  ",
                    "  1  ",
                    "  1  ",
                    "     ",
                    "  1  "]

QUESTION_MARK = [" 111 ",
                 "1   1",
                 "   1 ",
                 "  1  ",
                 "  1  ",
                 "     ",
                 "  1  "]

DOUBLE_QUOTE = [" 1 1 ",
                " 1 1 ",
                "     ",
                "     ",
                "     ",
                "     ",
                "     "]

SINGLE_QUOTE = ["  1  ",
                "  1  ",
                "     ",
                "     ",
                "     ",
                "     ",
                "     "]

APOSTROPHE = ["  1  ",
              "  1  ",
              "     ",
              "     ",
              "     ",
              "     ",
              "     "]

COMMA =      ["  1  ",
              "     ",
              "     ",
              " 11  ",
              " 11  ",
              "  1  ",
              " 1   "]

FULL_STOP = ["     ",
             "     ",
             "     ",
             "     ",
             "     ",
             " 11  ",
             " 11  "]

AT_SYMBOL = [" 111 ",
             "1   1",
             "1 111",
             "1 1 1",
             "1 1 1",
             "1 1 1",
             "1 111"]

HASH = [" 1 1 ",
        " 1 1 ",
        "11111",
        " 1 1 ",
        "11111",
        " 1 1 ",
        " 1 1 "]

TILDE = ["     ",
         "     ",
         "     ",
         " 1 1 ",
         "1 1  ",
         "     ",
         "     "]

COLON = ["     ",
         "  1  ",
         "  1  ",
         "     ",
         "     ",
         "  1  ",
         "  1  "]

SEMI_COLON = ["     ",
              "  1  ",
              "  1  ",
              "     ",
              "  1   ",
              "  1  ",
              " 11  "]

MORE_THAN = ["1    ",
             " 1   ",
             "  1  ",
             "   1 ",
             " 1   ",
             "1    ",
             "     "]

LESS_THAN = ["    1",
             "   1 ",
             "  1  ",
             " 1   ",
             "  1  ",
             "   1 ",
             "    1"]

EQUALS_SIGN = ["     ",
               "     ",
               "11111",
               "     ",
               "11111",
               "     ",
               "     "]

UNDERSCORE = ["     ",
              "     ",
              "     ",
              "     ",
              "     ",
              "     ",
              "11111"]

PERCENT = ["11   ",
           "11  1",
           "   1 ",
           "  1  ",
           " 1   ",
           "1  11",
           "   11"]

SPACE =      ["     ",
              "     ",
              "     ",
              "     ",
              "     ",
              "     ",
              "     "]

MAP_OF_ALPHANUM_TO_GLYPH = {'A':A,
                            'B':B,
                            'C':C,
                            'D':D,
                            'E':E,
                            'F':F,
                            'G':G,
                            'H':H,
                            'I':I,
                            'J':J,
                            'K':K,
                            'L':L,
                            'M':M,
                            'N':N,
                            'O':O,
                            'P':P,
                            'Q':Q,
                            'R':R,
                            'Q':Q,
                            'S':S,
                            'T':T,
                            'U':U,
                            'V':V,
                            'X':X,
                            'Y':Y,
                            'Z':Z,
                            'a':a,
                            'b':b,
                            'c':c,
                            'd':d,
                            'e':e,
                            'f':f,
                            'g':g,
                            'h':h,
                            'i':i,
                            'j':j,
                            'k':k,
                            'l':l,
                            'm':m,
                            'n':n,
                            'o':o,
                            'p':p,
                            'q':q,
                            'r':r,
                            's':s,
                            't':t,
                            'u':u,
                            'v':v,
                            'x':x,
                            'y':y,
                            'z':z,
                            '1':ONE_1,
                            '2':TWO_2,
                            '3':THREE_3,
                            '4':FOUR_4,
                            '5':FIVE_5,
                            '6':SIX_6,
                            '7':SEVEN_7,
                            '8':EIGHT_8,
                            '9':NINE_9,
                            '0':ZERO_0,
                            '(':BRACKET_OPEN,
                            ')':BRACKET_CLOSE,
                            '/':FORWARD_SLASH,
                            '_':UNDERSCORE,
                            '=':EQUALS_SIGN,
                            '<':LESS_THAN,
                            '>':MORE_THAN,
                            '~':TILDE,
                            ':':COLON,
                            ';':SEMI_COLON,
                            '@':AT_SYMBOL,
                            '#':HASH,
                            '\'':SINGLE_QUOTE,
                            '\"':DOUBLE_QUOTE,
                            ',':COMMA,
                            '.':FULL_STOP,
                            '\'':APOSTROPHE,
                            '?':QUESTION_MARK,
                            '!':EXCLAMATION_MARK,
                            '&':AMPERSAND,
                            '*':ASTERIX,
                            '^':CARET,
                            '+':PLUS,
                            '\u00A3':POUND_STERLING,
                            '$':DOLLAR_US,
                            '-':MINUS,
                            '%':PERCENT,
                            ' ':SPACE

}

def convert_character_to_glyph(character):
    print ('char', character)
    return MAP_OF_ALPHANUM_TO_GLYPH[character]
    
def create_character_at_coords_with_block_on_x_axis(character, xCoord, yCoord, zCoord, blockToUse):
    glyph = convert_character_to_glyph(character)
    print ('glyph', glyph)
    for y, row in enumerate(glyph):
        print ('y=', y, 'row', row)
        for x, column in enumerate(row):
            #check if glyph block should have a block, air or inverse
            print "col is", column
            print "x = ", x
            print column==1
            print column=='1'
            if(column == '1'):
                print "creating block"
                mc.setBlock(xCoord + (len(row)-x), yCoord + (len(glyph)-y) , zCoord, blockToUse)
            else:
                mc.setBlock(xCoord + (len(row)-x), yCoord + (len(glyph)-y) , zCoord, mc_block.AIR)

def print_string_to_world(string, lowerLeftX, lowerLeftY, lowerLeftZ, blockToUse):
    #iterate through the string per character writing into the world.
    x = lowerLeftX
    y = lowerLeftY
    z = lowerLeftZ
    for letter in string:
        create_character_at_coords_with_block_on_x_axis(letter, x, y, z, blockToUse)
        x -= 6


if __name__ == "__main__":
	
	mc = minecraft.Minecraft.create()
	pos = mc.player.getTilePos()
        numOfArgs = len(sys.argv)
        if numOfArgs == 2:
            print_string_to_world(sys.argv[1], pos.x+19, pos.y+1, pos.z+19, mc_block.WOOL.withData(2))
	elif numOfArgs == 3:
            blockIdAndData = sys.argv[2].split(',')
            blockId = int(blockIdAndData[0])
            blockData = int(blockIdAndData[1])
            blockToUse = mc_block.Block(blockId,blockData)
            print_string_to_world(sys.argv[1], pos.x+19, pos.y+1, pos.z+19, blockToUse)
        else:
             print("incorrect number of arguments")
             sys.exit()
