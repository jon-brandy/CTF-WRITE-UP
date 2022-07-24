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

