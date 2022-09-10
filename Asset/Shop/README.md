# Shop
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: [source](https://github.com/jon-brandy/CTF-WRITE-UP/blob/99ff48d928990503eb7ceaeb39ca31875b3a24ab/Asset/Shop/source). The shop is open for business at `nc mercury.picoctf.net 24851`.
## HINT:
- Always check edge cases when programming
## STEPS:
1. First, download the file given.
2. Now, let's check the file type.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/189481826-67c7af56-d10a-474b-be2a-ee2c97e6ca09.png)

3. Since it's an executable file and **not stripped**.
4. Let's run the file in gdb, but make it executable first by run -> `chmod +x source`.

> GDB

![image](https://user-images.githubusercontent.com/70703371/189481878-5eee7a22-7306-4703-a953-6b942582f8dd.png)

5. 
