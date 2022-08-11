# buffer overflow 1
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Control the return address Now we're cooking! 
You can overflow the buffer and return to the flag function in the [program](https://github.com/jon-brandy/CTF-WRITE-UP/blob/4b15b8791f8a6558c6fc8bfedeba343c9ab77ec7/Asset/buffer%20overflow%201/vuln). 
You can view source [here](). And connect with it using 
`nc saturn.picoctf.net 49449`.
## HINTS:
1. Make sure you consider big Endian vs small Endian.
2. Changing the address of the return pointer can call different functions.
## STEPS:
1. First
