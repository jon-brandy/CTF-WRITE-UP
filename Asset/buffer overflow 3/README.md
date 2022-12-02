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


12. 


9. Based 

