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
6. 

