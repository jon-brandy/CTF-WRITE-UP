# Here's a LIBC
> Write-up author: jon-brandy
## DESCRIPTION:
I am once again asking for you to pwn this binary vuln libc.so.6 Makefile nc mercury.picoctf.net 42072
## HINT:
1. PWNTools has a lot of useful features for getting offsets.
## STEPS:
1. Given a 64 bit binary file and the libc library.

![image](https://user-images.githubusercontent.com/70703371/223358966-7cf60cff-0c08-494c-9a00-5fdfd1d75206.png)


![image](https://user-images.githubusercontent.com/70703371/223359029-ea4e1434-370b-493f-bb2f-0e63350e8406.png)


2. Let's check it's protections then.

> VULN -> Partial RELRO, No Canary Found, No PIE.

![image](https://user-images.githubusercontent.com/70703371/223359201-b7035a95-3529-41ac-bc63-131855069c46.png)


3. Based from the challenge's title and the protections it has, we shall do **ret2libc attack**.
4. Let's make the binary executeable first then run it.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/223359504-53a443d5-44e2-4466-ac0f-8a5c0463ff2b.png)


5. Seems like we need to patch the binary in order to run it.
6. Luckily there's a tool named **pwninit** to patch the binary.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/223360625-16e97db6-3196-47b3-9e8f-94a2cafc3b3f.png)


![image](https://user-images.githubusercontent.com/70703371/223360687-0f801324-3df4-4a6c-a3d5-a100b73ac2ba.png)


7. Great! Now we have the patched binary file.
8. Let's try to run it now.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/223360953-abb6a2d8-9867-47c1-9054-00416d156b38.png)


9. It keeps prompt us an input.
10. Let's decompile the binary.

> vuln found at do_stuff() function

![image](https://user-images.githubusercontent.com/70703371/223361583-1f99a958-75ab-4249-a896-8cb08c2bdda3.png)


![image](https://user-images.githubusercontent.com/70703371/223361797-c73bf01b-50a9-4d3b-b59c-557e86f74a0e.png)


11. No filter for the `local_88` variable's scanf, means we can overflow the buffer here and control the **RIP**.
12. And for the `local_89` nothing special.

![image](https://user-images.githubusercontent.com/70703371/223362107-931e9354-4ede-4214-84e6-d9ec34125633.png)


13. The loop also won't be our interest here, because it just convert the case of our input.

![image](https://user-images.githubusercontent.com/70703371/223362543-2f610585-1702-4a6d-a624-27cd386337ef.png)


14. Notice we can leak the **libc runtime** using the puts call.

![image](https://user-images.githubusercontent.com/70703371/223362671-b762ae20-1b9b-42fc-a2c0-8c8f4deaf1d9.png)


15. Anyway let's get the **RIP** offset first.

> ENTER CYCLIC 1024 PATTERN

![image](https://user-images.githubusercontent.com/70703371/223362959-fa30a12b-9a39-470d-8838-58e08f5d60ca.png)


> USE THE LEAKED RSP BYTES 

![image](https://user-images.githubusercontent.com/70703371/223363070-91428397-976f-4cf5-9a19-d512620498d6.png)


16. Hence we need to enter 136 bytes as the padding.
17. Since we want to leak the **libc runtime** using the puts function, we have to make a **ROP** exploit where the `puts()` function shall call the puts. -> `puts(puts)`.
18. With this, the program shall printed out the address where `puts` is loaded inside the libc.
19. To do this we need `pop rdi` gadget, `puts@plt` offset and `puts@got` offset. We can automate the search with **pwntools**, but i prefered to do it manually.

> GET THE RDI -> 0x0000000000400913

![image](https://user-images.githubusercontent.com/70703371/223365336-cab343e4-20c4-49b7-878d-21fa116a1fd4.png)


> GET THE PUTS@PLT -> 0x400540

![image](https://user-images.githubusercontent.com/70703371/223365541-830ca543-3b8e-480d-b7ef-90f9bcc64b46.png)


> GET THE PUTS@GOT





