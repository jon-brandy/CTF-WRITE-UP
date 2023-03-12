# stack cache
> Write-up author: vrescho
## DESCRIPTION:
Undefined behaviours are fun. It looks like Dr. Oswal allowed buffer overflows again. 
Analyse this program to identify how you can get to the flag. You can view source here. 
And connect with it using nc saturn.picoctf.net 62780
## HINT:
1. Maybe there is content left over from stack?
2. Try compiling it with gcc and clang-12 to see how the binaries differ
## STEPS:
1. Given a not stripped 32 bit binary file.

![image](https://user-images.githubusercontent.com/70703371/224532660-e0cbdbc3-c664-475a-b252-7a70c462c579.png)


2. Let's check the binary protections.

> VULN -> Partial RELRO, No PIE.

![image](https://user-images.githubusercontent.com/70703371/224532691-aa3cfd20-48ff-4f32-93b9-26543a44cf82.png)


3. Now check the source code.

> SOURCE

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <wchar.h>
#include <locale.h>

#define BUFSIZE 16
#define FLAGSIZE 64
#define INPSIZE 10

/*
This program is compiled statically with clang-12
without any optimisations.
*/

void win() {
  char buf[FLAGSIZE];
  char filler[BUFSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f); // size bound read
}

void UnderConstruction() {
        // this function is under construction
        char consideration[BUFSIZE];
        char *demographic, *location, *identification, *session, *votes, *dependents;
	char *p,*q, *r;
	// *p = "Enter names";
	// *q = "Name 1";
	// *r = "Name 2";
        unsigned long *age;
	printf("User information : %p %p %p %p %p %p\n",demographic, location, identification, session, votes, dependents);
	printf("Names of user: %p %p %p\n", p,q,r);
        printf("Age of user: %p\n",age);
        fflush(stdout);
}

void vuln(){
   char buf[INPSIZE];
   printf("Give me a string that gets you the flag\n");
   gets(buf);
   printf("%s\n",buf);
   return;
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  vuln();
  printf("Bye!");
  return 0;
}

```

4. Based from it, we can control the **EIP** by overflow the buffer of var buf then return to the `win()` function, it's a simple ret2win concept then.
