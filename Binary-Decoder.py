
# Binary Decoder #Winkelmann
# libraries
import fileinput
import re

# ---------------- Functions -----------------------
# reads input from stdin, returns it to main
def readinput() :
     for line in fileinput.input() :
         line
         print("Original input: " + line)
         return line

# 7 bit decoder function
def decode7(input) :
    # separates every 7th bit
    holder = re.findall('.......', input)
    result = ""
    # convert each character and add it to resulting string
    for i in range(len(holder)) :
        result = result + chr(int(holder[i], 2))
        i += 1
    print("7 bit ASCII: " + result)

def decode8(input) :
    # separate every 8th bit
    holder = re.findall('........', input)
    result = ""
    # convert each character and add it to the resulting string
    for i in range(len(holder)) :
        result = result + chr(int(holder[i],2))
        i += 1
    print("8 bit ASCII: " + result)
# ----------- Main ---------------------------  
input = readinput()
decode7(input)
decode8(input)