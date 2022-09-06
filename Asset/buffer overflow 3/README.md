# buffer overflow 3
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Do you think you can bypass the protection and get the flag?
It looks like Dr. Oswal added a stack canary to this [program](https://github.com/jon-brandy/CTF-WRITE-UP/blob/d6703447a725fc59dc635aa42beeaee467577564/Asset/buffer%20overflow%203/vuln) to protect against buffer overflows. You can view source [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/d6703447a725fc59dc635aa42beeaee467577564/Asset/buffer%20overflow%203/vuln.c). 
And connect with it using: `nc saturn.picoctf.net 64367`
## HINT:
1. Maybe there's a smart way to brute-force the canary?
## STEPS:
1. First, download both files given.
2. Next, check the program file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/188170644-2e7f9941-965c-4286-807e-df16404ebcf1.png)

3. It's a 32 bit file and not stripped.
4. Let's make it executeable by run -> `chmod +x vuln` then check the protector by run `checksec --file vuln`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/188170952-6cd2b3fc-9860-4432-a0be-2169df4c1827.png)

5. Seems there's **no canary** & **no pie**, great!
6. Now let's analyze the source-code.

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
#define CANARY_SIZE 4

void win() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    fflush(stdout);
    exit(0);
  }

  fgets(buf,FLAGSIZE,f); // size bound read
  puts(buf);
  fflush(stdout);
}

char global_canary[CANARY_SIZE];
void read_canary() {
  FILE *f = fopen("canary.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'canary.txt' in this directory with your",
                    "own debugging canary.\n");
    fflush(stdout);
    exit(0);
  }

  fread(global_canary,sizeof(char),CANARY_SIZE,f);
  fclose(f);
}

void vuln(){
   char canary[CANARY_SIZE];
   char buf[BUFSIZE];
   char length[BUFSIZE];
   int count;
   int x = 0;
   memcpy(canary,global_canary,CANARY_SIZE);
   printf("How Many Bytes will You Write Into the Buffer?\n> ");
   while (x<BUFSIZE) {
      read(0,length+x,1);
      if (length[x]=='\n') break;
      x++;
   }
   sscanf(length,"%d",&count);

   printf("Input> ");
   read(0,buf,count);

   if (memcmp(canary,global_canary,CANARY_SIZE)) {
      printf("***** Stack Smashing Detected ***** : Canary Value Corrupt!\n"); // crash immediately
      fflush(stdout);
      exit(-1);
   }
   printf("Ok... Now Where's the Flag?\n");
   fflush(stdout);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  read_canary();
  vuln();
  return 0;
}

```

7. It seems we need to find the `win()` function's address.

![image](https://user-images.githubusercontent.com/70703371/188172478-79333a8c-77ab-46d1-a766-3b574b24b1ab.png)

8. And these part is quite interesting.

![image](https://user-images.githubusercontent.com/70703371/188172567-1d71dcbf-b669-49ae-97f6-e3f17be89f25.png)

![image](https://user-images.githubusercontent.com/70703371/188172710-681b4d70-526f-4101-9f73-cc981f987f4c.png)


9. Looks like there's a overflow check at the `vuln()` function.

![image](https://user-images.githubusercontent.com/70703371/188622192-402f89e7-d5ba-43b3-8bc2-8171ad5d66ed.png)

10. If the canary does not match the global canary then the program will detect that we tried to overflowing.
11. Now let's try to run the `program` file.

> RESULTS

![image](https://user-images.githubusercontent.com/70703371/188622563-f75f334d-df59-4e04-a531-03de2cab7836.png)

12. I input the text `FLAG{}` inside the `canary.txt`.
13. Now let's run it again.
14. 
