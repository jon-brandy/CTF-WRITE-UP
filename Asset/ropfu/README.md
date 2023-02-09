# ropfu
> Write-up author: vreshco
## DESCRIPTION:
What's ROP? Can you exploit the following program to get the flag? Download source. nc saturn.picoctf.net 56522
## HINT:
- NONE
## STEPS:
1. First, download the binary file given, then check the binary type and it's protections.

> TYPE - 32 bit, not stripped.

![image](https://user-images.githubusercontent.com/70703371/217817473-ecb19db2-e5c6-41a2-baad-1d5f05520313.png)

> VULN - Partial RELRO, NX Disabled, NO PIE, Has RWX segments. 

![image](https://user-images.githubusercontent.com/70703371/217817687-bcf2af08-a1d4-4a54-a41c-b82b226ab3cb.png)

