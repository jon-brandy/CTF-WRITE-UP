# asm1
#### Write-up author: [jon-brandy](https://github.com/jon-brandy) & [PlasmaRing](https://github.com/PlasmaRing)
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

> NOTES:

```
All the values in assembly are hexadecimal
```

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

5. To solve this, we need to read and follow the program.
6. At this part, we compare `0x2e0` (from the picoCTF description) to `0x3fb`.

![image](https://user-images.githubusercontent.com/70703371/180649431-f0f6d123-f4ad-43cb-b482-abf308deab93.png)

7. It is known `0x2e0` is lower than `0x3fb`. 
8. So we skip the `+10` line.
9. At line `+12`, compare `0x2e0` to `0x280`.
10. It is known that `0x2e0` is not equal to `0x280`.
11. So at line `+19` , we jump to line `+29`.

![image](https://user-images.githubusercontent.com/70703371/180649608-70103084-a810-4580-8361-9330b9c7cf25.png)

12. At line `+29`, the program fill the eax as `0x2e0`, then at line `+32`, the program substract `eax` to `0xa`. If you search at the internet for the result. We got -> **726**.
13. Then we jump to line `+60` and the program do exit.

![image](https://user-images.githubusercontent.com/70703371/180650236-9ee5c87b-bb64-4d75-840d-d934ded4e3f2.png)

14. Finally we just have to convert the integer result to hexadecimal.
15. For this solution i used python code.

```py

import os

os.system("cls")
num = 726
print(hex(num))

```

> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/180650345-71d41365-2ac6-48db-93b4-1cab376ca238.png)



---
## FLAG

```
0x2d6
```

## REFERENCES:

```
https://stackoverflow.com/questions/25658069/what-does-mov-eax-dword-ptr-eax-do
```

