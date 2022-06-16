# buffer overflow 0
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Smash the stack Let's start off simple, can you overflow the correct buffer? 
The program is available [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/3505b54dcda38d2f82a13a3f0c10dca01ed65735/Asset/buffer%20overflow%200/vuln). You can view source [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/3505b54dcda38d2f82a13a3f0c10dca01ed65735/Asset/buffer%20overflow%200/vuln.c). 
And connect with it using: 
`nc saturn.picoctf.net 51110`

## HINTS:
1. How can you trigger the flag to print?
2. If you try to do the math by hand, maybe try and add a few more characters. Sometimes there are things you aren't expecting.
3. Run man gets and read the BUGS section. How many characters can the program really read?

## STEPS:


