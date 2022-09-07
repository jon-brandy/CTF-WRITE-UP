# x-sixty-what
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Overflow x64 code 
Most problems before this are 32-bit x86.
Now we'll consider 64-bit x86 which is a little different! 
Overflow the buffer and change the return address to the `flag` function in this [program](https://github.com/jon-brandy/CTF-WRITE-UP/blob/74b33b7a185cb1fe916b413629149156f6765323/Asset/x-sixty-what/vuln). 
Download [source](https://github.com/jon-brandy/CTF-WRITE-UP/blob/74b33b7a185cb1fe916b413629149156f6765323/Asset/x-sixty-what/vuln.c). `nc saturn.picoctf.net 59713`
## HINTS:
1. Now that we're in 64-bit, what used to be 4 bytes, now may be 8 bytes.
2. Jump to the second instruction (the one after the first push) in the flag function, if you're getting mysterious segmentation faults.
## STEPS:
1. First, download both files given.
2. Next, let's whether the `program` file is stripped or not.

![image](https://user-images.githubusercontent.com/70703371/188832877-c1e6aeae-c8aa-4c98-acd2-f12fcde02077.png)

3. Great! Since it's not stripped so we can see all the functions name.
4. Now let's check the file protection.

![image](https://user-images.githubusercontent.com/70703371/188836157-9252437e-dff0-41d5-960b-45c88ed21166.png)

5. **No pie** and **no canary**, seems we can use the same method as usual.
6. But let's run the program, but make it executeable first by run -> `chmod +x vuln`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/188836557-0d6a510f-3c51-48c1-96bf-eddbfb322dc9.png)

7. Now let's analyze the source code.

> VULN.C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFFSIZE 64
#define FLAGSIZE 64

void flag() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  printf(buf);
}

void vuln(){
  char buf[BUFFSIZE];
  gets(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  puts("Welcome to 64-bit. Give me a string that gets you the flag: ");
  vuln();
  return 0;
}

```

8. At the `vuln()` function, we can take advantage of the `gets()` function to do bufferoverflow.

![image](https://user-images.githubusercontent.com/70703371/188837621-3209223f-60c9-42ff-af39-eda4e688d98e.png)

9. Since we can't see what address we jumped to, let's run the program using gdb and create pattern of strings.

![image](https://user-images.githubusercontent.com/70703371/188853146-978f0577-35e5-49e4-9271-3b2328640110.png)

10. Copy the strings, now run the program and paste the strings as input.

> RESULTS

![image](https://user-images.githubusercontent.com/70703371/188853468-31758b86-5ddf-4dc3-a559-9cae8b4559fd.png)

![image](https://user-images.githubusercontent.com/70703371/188853500-d2c10f45-f3b0-442e-8a8a-bf6c7e2f81f2.png)

11. Notice here, somehow **rip** does not have our input.

![image](https://user-images.githubusercontent.com/70703371/188854058-6e90c4d1-ba23-47ff-8ad5-c17670eb579a.png)

12. 
