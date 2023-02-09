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

> VULN - Partial RELRO (can read & write GOT), NX Disabled (can perform bufferoverflow with code execution from memory that marked as NX), NO PIE (ASLR disabled), Has RWX segments (allows us to inject shellcode & execute it). 

![image](https://user-images.githubusercontent.com/70703371/217817687-bcf2af08-a1d4-4a54-a41c-b82b226ab3cb.png)


2. Next, let's see the source code given.
3. Notice, at the `vuln()` function, we can do bufferoverflow.

![image](https://user-images.githubusercontent.com/70703371/217821110-61ff4078-48c4-4c2c-90e1-ceef8d3a5d72.png)


4. But the problem is, there's no flag function or any interesting function to jump.
5. Anyway let's find the correct offset first for EIP.
6. Let's run the binary using **pwndbg**, then enter cyclic 100 bytes as input.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/217822357-d7263cbe-6784-4361-b4fa-b68b8123c0bf.png)


![image](https://user-images.githubusercontent.com/70703371/217822396-c1009e7e-5033-4585-a004-afd2ccae8870.png)


7. Got segmentation fault, to find the offset, let's copy the 4 characters from the EIP.

> RESULT - 28

![image](https://user-images.githubusercontent.com/70703371/217822580-59b36ecb-b6e5-418d-9fd9-76765e26e4cc.png)


8. g
