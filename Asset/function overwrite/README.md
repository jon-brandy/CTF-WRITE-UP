# function overwrite
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Story telling class 2/2 
You can point to all kinds of things in C. 
Checkout our function pointers demo [program](https://github.com/jon-brandy/CTF-WRITE-UP/blob/47628a61a917b3ed17b6fa3cd5ea8543d4991c4f/Asset/function%20overwrite/vuln). You can view source [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/47628a61a917b3ed17b6fa3cd5ea8543d4991c4f/Asset/function%20overwrite/vuln.c). 
And connect with it using `nc saturn.picoctf.net 54627`
## HINT:
1. Don't be so negative
## STEPS:
1. First, download both files given.
2. Next, let's check the file type of the `program`.

> RESULT


![image](https://user-images.githubusercontent.com/70703371/189645861-3bf1b93a-dbc4-453a-84ab-25efe35503ab.png)


3. It's an ELF 32 bit and **not stripped** , means we can see the functions name.
4. Now let's check the file protector.

> RESULT


![image](https://user-images.githubusercontent.com/70703371/189645915-39435f02-0d7e-4655-aeca-074aac836f33.png)


5. **No canary** and **no pie**.
6. Let's make the program executeable by run ->  `chmod +x vuln`.
7. Now let's run the program without the gdb.
8. Let's input values the program want.

![image](https://user-images.githubusercontent.com/70703371/189645969-8fe297d5-7054-4a6b-8b37-a9ddd0fc1ee1.png)


9.
