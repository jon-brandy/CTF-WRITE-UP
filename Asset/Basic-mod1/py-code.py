import os

os.system("cls")
arr = [202, 137, 390, 235, 114, 369, 198, 110, 350, 396, 390, 383,
       225, 258, 38, 291, 75, 324, 401, 142, 288, 397] #list of numbers from the message.txt
secnArr = [] #second array variable
for items in arr: #loop through the list of numbers
    secnArr = items % 37 #modulus 37 to get the remainder
    print(secnArr, end = " ") #print the remainder in one line

#Character map mentioned from the description
'''
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
'''

