# gogo
> Write-up author: jon-brandy
## DESCRIPTION:
Hmmm this is a weird file... enter_password. There is a instance of the service running at mercury.picoctf.net:4052.
## HINT:
1. use go tool objdump or ghidra
## STEPS:
1. Given a not stripped 32 bit binary file.

![image](https://user-images.githubusercontent.com/70703371/222879607-02ae53a9-ca9c-4bfe-a89c-3b2921a5e763.png)


2. Let's run the binary.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/222879656-f9b34581-5262-404e-9c59-15b292194640.png)


3. Let's decompile the binary.
4. Analyzing the **main.main()** function, notice the **checkPassword()** called.

![image](https://user-images.githubusercontent.com/70703371/222879745-dfa0edf6-ab13-48d0-83c4-ba041bdafe00.png)


5. Now check that.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/222879775-c4215fbb-404e-4fbb-959a-a4858848bc10.png)


6. Found a XOR operation.

![image](https://user-images.githubusercontent.com/70703371/222879915-5b76d520-1fd3-475c-9d91-24df13195c88.png)


7. Open gdb and set a breakpoint at this offset -> `0x080d4b2d` (offset of xchg instruction -> eax, ebp) so we can see key value stored in **esi+0x4** and the expected values (which stored in esi+0x24). 

> RESULT -> GDB

![image](https://user-images.githubusercontent.com/70703371/222880536-d4e17262-640d-46d0-8ecc-41db4fba9045.png)


8. For the strings we need to enter 32 bytes.

> REASON

![image](https://user-images.githubusercontent.com/70703371/222880545-e04d8140-eab9-45ab-a490-d3ff34ce0465.png)


> RESULT

![image](https://user-images.githubusercontent.com/70703371/222880573-71330045-3589-4174-8db3-9dbb12226a63.png)


![image](https://user-images.githubusercontent.com/70703371/222880591-07b9d6eb-ae8b-43a1-99c2-54307be61011.png)


9. Hexdump at the offset of **esp+0x4**.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/222880626-dfa3236d-ecba-48e9-869b-7941ac475352.png)


> WHY 0X4?

![image](https://user-images.githubusercontent.com/70703371/222880665-21d22eb3-18b7-4656-a9d0-cf6bec252d2c.png)


- They moved the key (stored in esi+0x4) to esi.
- Then used the key to XOR the strings stored in ebp.

10. Hence now we know the key used is -> `861836f13e3d627dfa375bdb8389214e`.

![image](https://user-images.githubusercontent.com/70703371/222880710-5e1d3ee2-13ca-4e6c-824d-f15cba1708ac.png)


11. Then the ex




