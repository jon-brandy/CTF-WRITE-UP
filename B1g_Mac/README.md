# B1g_Mac
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Here's a [zip file](https://jupiter.challenges.picoctf.org/static/2b1cf2a4a463b1a3e031d2fcef3fa54d/b1g_mac.zip).
## HINT:
- NONE
## STEPS:
1. First, download the `.zip` file given.
2. Next, unzip the file.

![image](https://user-images.githubusercontent.com/70703371/192094181-34ef85eb-ec23-44b5-9c85-4a5bab2055f8.png)


3. It seems we got 1 directory named `test` and 1 PE32 file named `main.exe`.
4. Anyway, let's run the `.exe` file on windows.

> AT THE CMD

![image](https://user-images.githubusercontent.com/70703371/192096744-de453ca7-b6ce-4445-b909-e362dbac36da.png)

5. It says no flag found, because we didn't run it on the server but we run it on a client.
6. Let's decompile it using **ghidra**

> GHIDRA

![image](https://user-images.githubusercontent.com/70703371/192098667-a0d5551d-90c6-4ecb-ba83-11f1cd3e76c2.png)

7. View the main function first.

> MAIN

![image](https://user-images.githubusercontent.com/70703371/192098937-602ba58a-f6d8-4ed9-b3a0-8ddfb70f1d8d.png)

8. Notice here, we have to make a file called `flag.txt`.

![image](https://user-images.githubusercontent.com/70703371/192099114-8622156b-ac0a-487f-98d8-3a11e1105989.png)

9. This part caught my attention.

![image](https://user-images.githubusercontent.com/70703371/192099145-9985a6bf-af0e-4434-ab11-364728a950a4.png)

10. 


