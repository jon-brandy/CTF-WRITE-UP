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
1. First, download the `.exe` file and the `source code` to see how the program works.
2. Now, open the `.c` file first.

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

3. Based from the hint given, let's try to enter input characters more than the specified limit.
4. On your kali linux terminal, type this command `nc saturn.picoctf.net 51110`.

![Screenshot (444)](https://user-images.githubusercontent.com/70703371/174065135-7b9cd229-ce42-4e23-bc96-9be9b9a2b307.png)

6. Then enter more than 16 characters to make it gets **buffer overflows**.
7. This time i tried to input 18 characters, but the program still gave me this output. Which means it's not overflowed.

![Screenshot (446)](https://user-images.githubusercontent.com/70703371/174065766-7610c458-689c-4ac9-a4cb-d92af3cd7137.png)

8. Now try to enter much more characters.

![Screenshot (447)](https://user-images.githubusercontent.com/70703371/174066142-c9c918ff-7c54-4bf3-8347-b62a4dc418d7.png)

9. As you can see, from the image above, we got no output.
10. Now try to enter much more characters!

![Screenshot (448)](https://user-images.githubusercontent.com/70703371/174066328-0dc638e9-08d6-42bd-8d8d-e18fd67e3134.png)

11. Finally it became buffer overflowed and we got the flag!


---

```
picoCTF{ov3rfl0ws_ar3nt_that_bad_8ba275ff}
```
