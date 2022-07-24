# asm1
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
What does asm1(0x2e0) return? 
Submit the flag as a hexadecimal value (starting with '0x'). 
NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://github.com/jon-brandy/CTF-WRITE-UP/blob/c22ac49a6c1aa41d84deed5a985052e46d48dd23/Asset/asm1/test.S)
## HINT:
1. assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)
## STEPS:
1. First, download the file given.
2. Next check the file type by run -> `file test.S`.

![image](https://user-images.githubusercontent.com/70703371/180635753-71002eee-4b3b-4c1d-b42d-a07639aca927.png)

3. Since it's an ASCII text file, let's see what's inside by run -> `strings test.S`.

![image](https://user-images.githubusercontent.com/70703371/180635782-781fbcf9-095c-499d-b84d-f4dd24d82ed4.png)

4. Looks like it's an assembly code.

```asm
asm1:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x3fb
	<+10>:	jg     0x512 <asm1+37>
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x280
	<+19>:	jne    0x50a <asm1+29>
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
	<+24>:	add    eax,0xa
	<+27>:	jmp    0x529 <asm1+60>
	<+29>:	mov    eax,DWORD PTR [ebp+0x8]
	<+32>:	sub    eax,0xa
	<+35>:	jmp    0x529 <asm1+60>
	<+37>:	cmp    DWORD PTR [ebp+0x8],0x559
	<+44>:	jne    0x523 <asm1+54>
	<+46>:	mov    eax,DWORD PTR [ebp+0x8]
	<+49>:	sub    eax,0xa
	<+52>:	jmp    0x529 <asm1+60>
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,0xa
	<+60>:	pop    ebp
	<+61>:	ret    

```
