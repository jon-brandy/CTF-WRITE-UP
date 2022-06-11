# Basic-mod2
## DESCRIPTION:
A new modular challenge! Download the message [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/295e948fa9ea37bd6b1c73dd24718f146e776576/Asset/Basic-mod2/message.txt). 
Take each number mod 41 and find the modular inverse for the result. 
Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. 
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
## HINTS:
1. Do you know what the modular inverse is?
2. The inverse modulo z of x is the number, y that when multiplied by x is 1 modulo z.
3. It's recommended to use a tool to find the modular inverses
## STEPS:
1. First, download the `message.txt` file.

```
104, 290, 356, 313, 262, 337, 354, 229, 146, 297, 118, 373, 221, 359, 338, 321, 288, 79, 214, 277, 131, 190, 377
```

3. The pattern quite similiar to the previous one, the `basic-mod1` challenge. But for this one, we use the modular inverse algorithm.
4. I tried to solve it using python code like this:

```py
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
```

5. Finally, after executed the file, we got the flag!

![Screenshot (117)](https://user-images.githubusercontent.com/98648342/173170278-6c168b55-a4ac-4b44-ac16-2989278d8122.png)


---

## FLAG:
```
picoCTF{1nv3r53ly_h4rd_8a05d939}
```
