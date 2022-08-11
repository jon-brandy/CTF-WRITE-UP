# buffer overflow 1
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Control the return address Now we're cooking! 
You can overflow the buffer and return to the flag function in the [program](https://github.com/jon-brandy/CTF-WRITE-UP/blob/4b15b8791f8a6558c6fc8bfedeba343c9ab77ec7/Asset/buffer%20overflow%201/vuln). 
You can view source [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/9cda637bea2a85da46ba8dce3c9ccf131928092f/Asset/buffer%20overflow%201/vuln.c). And connect with it using 
`nc saturn.picoctf.net 49449`.
## HINTS:
1. Make sure you consider big Endian vs small Endian.
2. Changing the address of the return pointer can call different functions.
## STEPS:
1. First, download both file given.
2. Next, check the program, is it executeable or not.

![image](https://user-images.githubusercontent.com/70703371/184164409-dfc35fd8-6e24-4756-832e-de899e682792.png)

3. Seems we can make it executable and nicely it's not stripped, so we can see the function.
4. But before make it executeable, let's check are there any protection on the file.
5. Run -> `checksec --file vuln`.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/184164974-2c09f927-035a-4b92-af20-35eaeca03ca3.png)

6. Seems like there's no protection, which means there's many solutions available here.

```
WE MAY:

Do bufferoverflow
Inject shellcode
````

7. But let's decompile it first, i used `IDA` to decompile it.


