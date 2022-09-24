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
6. Let's decompile it using IDA.

> IDA


