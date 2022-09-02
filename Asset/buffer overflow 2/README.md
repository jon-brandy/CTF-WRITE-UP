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

