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

> 

