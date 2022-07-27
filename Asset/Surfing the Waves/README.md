# Surfing the Waves
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
While you're going through the FBI's servers, you stumble across their incredible taste in music. 
One [main.wav](https://github.com/jon-brandy/CTF-WRITE-UP/blob/085d332b36324036d253e273371183a147e784f0/Asset/Surfing%20the%20Waves/main.wav) you found is particularly interesting, see if you can find the flag!
## HINTS:
1. Music is cool, but what other kinds of waves are there?
2. Look deep below the surface
## STEPS:
1. First, download the file given.
2. Next, i opened the file in Audacity.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/181199083-1f609c55-e63f-40ae-bba3-ffd25184a34e.png)

3. It looks like there is some kind of pattern in the file.
4. For this solution i used `scipy.io` to read WAV file and collect all amplitudes.

> CODE

```py
import os
from scipy.io import wavfile

os.system("cls")
sampleRate, audioData = wavfile.read('main.wav') # LOAD THE AUDIO FILE

roundedData = []
unique = []
for i in audioData: # ROUND THE DATA
    result = round(i, -2) # ROUND TO THE NEAREST 0.01
    roundedData.append(result) # APPEND THE ROUNDED DATA
    if result in unique: # IF THE NUMBER IS ALREADY IN THE LIST, SKIP IT
        continue
    else: # if the number is not in the list, add it
        unique.append(result) 
unique.sort() # SORT THE UNIQUE VALUES

hexFlag = [] # HEX FLAG
for a in roundedData: # CONVERT THE DATA TO HEX
    hexFlag.append(hex(unique.index(a))[2:]) # APPEND THE HEX VALUE

print(bytearray.fromhex("".join(hexFlag)).decode()) # PRINT THE HEX FLAG
```

> OUTPUT

```
#!/usr/bin/env python3
import numpy as np
from scipy.io.wavfile import write
from binascii import hexlify
from random import random

with open('generate_wav.py', 'rb') as f:
        content = f.read()
        f.close()

# Convert this program into an array of hex values
hex_stuff = (list(hexlify(content).decode("utf-8")))

# Loop through the each character, and convert the hex a-f characters to 10-15
for i in range(len(hex_stuff)):
        if hex_stuff[i] == 'a':
                hex_stuff[i] = 10
        elif hex_stuff[i] == 'b':
                hex_stuff[i] = 11
        elif hex_stuff[i] == 'c':
                hex_stuff[i] = 12
        elif hex_stuff[i] == 'd':
                hex_stuff[i] = 13
        elif hex_stuff[i] == 'e':
                hex_stuff[i] = 14
        elif hex_stuff[i] == 'f':
                hex_stuff[i] = 15

        # To make the program actually audible, 100 hertz is added from the beginning, then the number is multiplied by        # 500 hertz
        # Plus a cheeky random amount of noise
        hex_stuff[i] = 1000 + int(hex_stuff[i]) * 500 + (10 * random())


def sound_generation(name, rand_hex):
        # The hex array is converted to a 16 bit integer array
        scaled = np.int16(np.array(hex_stuff))
        # Sci Pi then writes the numpy array into a wav file
        write(name, len(hex_stuff), scaled)
        randomness = rand_hex


# Pump up the music!
# print("Generating main.wav...")
# sound_generation('main.wav')
# print("Generation complete!")

# Your ears have been blessed
# picoCTF{mU21C_1s_1337_c1faf2a7}
```

5. Finally we got the flag!

---
## FLAG

```
picoCTF{mU21C_1s_1337_c1faf2a7}
```

**NOTES**: BIG THANKS TO -> [HHousen](https://github.com/HHousen) who helped me solve this challenge.

## REFERENCES

```
https://stackoverflow.com/questions/13039846/what-do-the-bytes-in-a-wav-file-represent
https://github.com/HHousen/PicoCTF-2021/blob/6f9f20933e1ed467dbdfcdd7af027a06439e2d84/Forensics/Surfing%20the%20Waves/README.md
```
