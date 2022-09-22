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
2. Next, let's check the program file BIT and whether the file is stripped or not.

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

7. We can take advantage of the `gets()` function to do buffer overflow.

![image](https://user-images.githubusercontent.com/70703371/191661030-84fa11ae-61ca-4b3c-912d-af088a1907a1.png)

> VULN FUNCTION

![image](https://user-images.githubusercontent.com/70703371/191661949-82aea034-a405-4d36-8fca-8cae1e488500.png)

8. So the goals here, we don't need to change the return address, we just have to bufferoverflow the input so the program crashed.

![image](https://user-images.githubusercontent.com/70703371/191663182-14b0c269-0be4-4bc4-93fc-217da6683660.png)


10. With that being said, the `sigsev` function triggered.

![image](https://user-images.githubusercontent.com/70703371/191661091-f8b665ba-e6c7-4cc7-a251-69dc564dca10.png)

10. Now let's create a `flag.txt` file and insert `FLAG{}` as the input.

![image](https://user-images.githubusercontent.com/70703371/191662063-9b5052bc-cce2-4fad-a3a8-055661b4c643.png)


![image](https://user-images.githubusercontent.com/70703371/191661564-77c87842-13ec-487d-b967-7178bcf7d0ba.png)

11. Make the `vuln` file executable by run `chmod +x vuln`.
12. Now run the file and input **100** A's.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/191663241-0993e007-1e49-4624-91be-f2066a2c98b9.png)


12. Run the `netcat` given and input the same A's length.

![image](https://user-images.githubusercontent.com/70703371/191663372-efdec55d-79c9-46f2-b9fb-3cdc4ddacaec.png)

13. We got the flag!

## FLAG

```
picoCTF{ov3rfl0ws_ar3nt_that_bad_8ba275ff}
```
