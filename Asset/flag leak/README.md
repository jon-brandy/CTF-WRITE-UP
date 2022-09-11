# flag leak
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Story telling class 1/2 
I'm just copying and pasting with this [program](https://github.com/jon-brandy/CTF-WRITE-UP/blob/0782a0d972e244a18c82cbc1c62c2d363bef0c61/Asset/flag%20leak/vuln). what can go wrong? You can view source [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/0782a0d972e244a18c82cbc1c62c2d363bef0c61/Asset/flag%20leak/vuln.c). 
And connect with it using: `nc saturn.picoctf.net 61389`
## HINT:
1. Format Strings
## STEPS:
1. First, download both files given.
2. Next, let's check the `program`'s file type.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/189511862-1198436f-b5f9-4742-ac12-504e6a9905a4.png)

3. Notice, it's a 32 bit file and not stripped, so we can see the functions name
4. Now check the file protection.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/189511913-7206d52a-f6da-4424-afa0-76d84d31a802.png)

5. **No canary found** and **no pie**. So they will keep the same memory location.
6. Now let's run the program but make it executable first by run -> `chmod +x vuln`.

> RUN

![image](https://user-images.githubusercontent.com/70703371/189511953-8c084cba-c734-4129-940c-7e4a117602fa.png)

7. Let's create `flag.txt` file first, then run the program again.

![image](https://user-images.githubusercontent.com/70703371/189511980-4beb33e4-5c09-4b38-81d2-24d07714d14c.png)

![image](https://user-images.githubusercontent.com/70703371/189512037-78b9c5a6-0361-4196-9105-95ee2676d144.png)


8. Hmm let's analyze the source code.

> VULN.C

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

void readflag(char* buf, size_t len) {
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,len,f); // size bound read
}

void vuln(){
   char flag[BUFSIZE];
   char story[128];

   readflag(flag, FLAGSIZE);

   printf("Tell me a story and then I'll tell you one >> ");
   scanf("%127s", story);
   printf("Here's a story - \n");
   printf(story);
   printf("\n");
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  vuln();
  return 0;
}
```

9. 
