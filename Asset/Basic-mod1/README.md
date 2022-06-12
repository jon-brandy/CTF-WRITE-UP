# Basic-mod1
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
We found this weird message being passed around on the servers, we think we have a working decryption scheme. 
Download the message [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/bc1c3f33cf96e7ec50e563fe8933d516d46f9c41/Asset/Basic-mod1/message.txt). Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 
26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the 
picoCTF flag format (i.e. picoCTF{decrypted_message})
## HINTS:
1. Do you know what mod 37 means?
2. mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.
## STEPS:
1. First, download the `.txt` file first, then try to mod all of them either manually or using python code.

```py
import os

os.system("cls")
arr = [202, 137, 390, 235, 114, 369, 198, 110, 350, 396, 390, 383,
       225, 258, 38, 291, 75, 324, 401, 142, 288, 397] #list of numbers from the message.txt
secnArr = [] #second array variable
for items in arr: #loop through the list of numbers
    secnArr = items % 37 #modulus 37 to get the remainder
    print(secnArr, end = " ") #print the remainder in one line
```

2. After the code executed, we got the remainder:

![Screenshot (440)](https://user-images.githubusercontent.com/70703371/173085006-fa476ae1-4296-4d20-b9db-0c0e20aef759.png)

```
17 26 20 13 3 36 13 36 17 26 20 13 3 36 1 32 1 28 31 31 29 27
```

3. Next, based from the description, try to use this mapping:

```
A: 0
B: 1
C: 2
D: 3
E: 4
F: 5
G: 6
H: 7
I: 8
J: 9
K: 10
L: 11
M: 12
N: 13
O: 14
P: 15
Q: 16
R: 17
S: 18
T: 19
U: 20
V: 21
W: 22
X: 23
Y: 24
Z: 25
0: 26
1: 27
2: 28
3: 29
4: 30
5: 31
6: 32
7: 33
8: 34
9: 35
_: 36
```

4. After mapped the numbers to the respective characters mentioned based from the description clue. We got this string:

```
R 0 U N D _ N _ R 0 U N D _ B 6 B 2 5 5 3 1
```

5. Well, it is the flag! we just have to wrap the string around with `picoCTF{}` and remember to remove the space between each character.


---

## FLAG:
```
picoCTF{R0UND_N_R0UND_B6B25531}
```
