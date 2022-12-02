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


