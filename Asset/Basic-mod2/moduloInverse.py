import os
import string
import math

os.system("cls")
stringChar = string.ascii_lowercase # string of all lowercase letters
stringChar += "0123456789_" # string of all lowercase letters and numbers
rawFlag = [104, 290, 356, 313, 262, 337, 354, 229, # raw flag
           146, 297, 118, 373, 221, 359, 338, 321,
           288, 79, 214, 277, 131, 190, 377]
convertedFlag = "" # converted flag variable

# convert raw flag to string of all lowercase letters and numbers
for items in rawFlag:
    index = pow(items, -1, 41) # convert to index of stringChar (mod 41)
    convertedFlag += stringChar[index - 1] # convert to character and add to string

print(convertedFlag) # print converted flag
