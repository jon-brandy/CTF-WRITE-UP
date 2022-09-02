# buffer overflow 2
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Control the return address and arguments This time you'll need to control the arguments to the function you return to! 
Can you get the flag from this [program?](https://github.com/jon-brandy/CTF-WRITE-UP/blob/f4988ca3e1525733628e10f39c3873e83589c97f/Asset/buffer%20overflow%202/vuln) 
You can view source [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/f4988ca3e1525733628e10f39c3873e83589c97f/Asset/buffer%20overflow%202/vuln.c). And connect with it using `nc saturn.picoctf.net 53709`.
## HINT:
1. Try using GDB to print out the stack once you write to it.
## STEPS:
1. First, download both files given.
2. Next let's check the program file by run `file vuln`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/188063140-c8571087-3b43-4285-a497-fc02f80176ac.png)

3. Since it's not stripped we can see the function in gdb then, also notice this time the file is 32 bit.
4. But i want to check the protector available here, so let's run `checksec --file vuln`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/188063279-a839274b-0c72-46ac-adad-983d54e0aaf2.png)

5. Great **no canary** found and **no pie**.
6. Now let's analyze the source code first.

> VULN.C  

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 100
#define FLAGSIZE 64

void win(unsigned int arg1, unsigned int arg2) {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  if (arg1 != 0xCAFEF00D)
    return;
  if (arg2 != 0xF00DF00D)
    return;
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);
  puts(buf);
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

7. Found the vuln here because of the `gets()` function.

![image](https://user-images.githubusercontent.com/70703371/188063545-c5fbdb3d-339a-4b33-b167-e14efef15c09.png)

8. I think this challenge is quite similiar to the previous one, but based from the description we need to control the arguments too not just the return address.
9. The win function caught my attention, because of the condition we must to fullfill to get the flag. 

![image](https://user-images.githubusercontent.com/70703371/188063795-b1c206bc-c2fd-4e19-87d4-fd8cfdddf37a.png)

> NOTES

```
arg1 must be -> 0xCAFEF00D
arg2 must be -> 0xF00DF00D
```

10. Anyway let's get the **win()** function's address first by run `gdb`.

> STEPS

![image](https://user-images.githubusercontent.com/70703371/188064249-f34a5f04-ef34-424a-8a08-92665044f17d.png)

![image](https://user-images.githubusercontent.com/70703371/188064277-23c6d1b1-9a53-4851-93b1-33c2bd3b7662.png)

```
win() address -> 0x8049296
```

11. Now let's run the program.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/188069254-a10261de-a5f7-4413-8b33-715daec8e591.png)

12. Let's try to input the same size as the buffer -> 100.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/188069350-40a8a62d-e1fe-444f-9775-0c9da587e507.png)

13. Let's add another 4 bytes.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/188069415-4e7143ae-2d77-42f7-92b1-a5e6a9d800a7.png)

14. Add another 4 bytes again.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/188069527-ecac073e-59e2-469a-adee-6a51c025a3e0.png)

15. Great the program crashed.
16. But at this point we didn't know did we just change the return address or not. 
17. So we need to find the `offset` of the **EIP**.

> NOTES

```
A standard buffer overflow is used to overwrite the EIP. It is usually possible to predict an appropriate EIP value that will land execution within 
the NOPs which will “execute” until the payload (usually shellcode) is encountered. 
• The shellcode then spawns a process to download and execute malware.
```

18.

## REFERENCES:

```
https://www.sciencedirect.com/topics/computer-science/extended-instruction-pointer
```
