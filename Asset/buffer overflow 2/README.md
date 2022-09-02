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

3. Since it's not stripped we can see the function in gdb then.
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

7. 
