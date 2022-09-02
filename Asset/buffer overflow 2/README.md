# buffer overflow 2
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Control the return address and arguments This time you'll need to control the arguments to the function you return to! 
Can you get the flag from this [program?]() 
You can view source [here](). And connect with it using `nc saturn.picoctf.net 53709`.
## HINT:
1. Try using GDB to print out the stack once you write to it.
## STEPS:
1. First, download both files given.
2. Next let's check the program file by run `file vuln`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/188063140-c8571087-3b43-4285-a497-fc02f80176ac.png)

3. Since it's not stripped we can see the function in gdb then.
4. But i want to check the protector available here, so let's run `checksec --file vuln`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/188063279-a839274b-0c72-46ac-adad-983d54e0aaf2.png)

5. Great **no canary** found and **no pie**.
6. Now let's analyze the source code first.

> VULN.C  


