# buffer overflow 0
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
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
2. Next, let's check the program file BIT and is it stripped or not.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/191660096-6b8c60dc-a7a6-4ff7-9d9c-480cf78aac97.png)

3. Seems it's a 32 BIT file and luckily it's not stripped, so we can see the function names.
4. Now let's check the file protection by run `checksec`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/191660229-44bb72b7-ee97-49a6-91bb-c3d4260358ca.png)

5. **No canary** means we can do bufferoverflow and **pie enabled** means the offset won't be the same.
6. Now let's analyze the source code.

> VULN.C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

#define FLAGSIZE_MAX 64

char flag[FLAGSIZE_MAX];

void sigsegv_handler(int sig) {
  printf("%s\n", flag);
  fflush(stdout);
  exit(1);
}

void vuln(char *input){
  char buf2[16];
  strcpy(buf2, input);
}

int main(int argc, char **argv){
  
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }
  
  fgets(flag,FLAGSIZE_MAX,f);
  signal(SIGSEGV, sigsegv_handler); // Set up signal handler
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);


  printf("Input: ");
  fflush(stdout);
  char buf1[100];
  gets(buf1); 
  vuln(buf1);
  printf("The program will exit now\n");
  return 0;
}

```

7. 
