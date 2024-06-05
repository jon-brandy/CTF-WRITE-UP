# VNE
> Write-up author: jon-brandy

## DESCRIPTION:
<p align="justify">We've got a binary that can list directories as root, try it out !! ssh to saturn.picoctf.net:59395, and run the binary named "bin" once connected. Login as ctf-player with the password, d137d16e</p>

## HINT:
- Have you checked the content of the /root folder.
- Find a way to add more instructions to the ls.

## STEPS:
1. In this challenge, we're not given both the binary and the source code. However, we're given a network connection and asked to execute a binary named **bin** in the shell.

> RESULT

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/c251a3d7-5c83-4fa8-b6bd-3e4b3b6940c8)


2. Based from the hint, the flag stored inside the `/root` directory, but we need to find a way around because access to root directory is not permitted.
3. BUT, seems the `bin` binary can also executed as root user.

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/cd3688f6-19f2-44a0-b28d-8baa16004f0f)


4. This should be our interest, then executing the binary gave us an output about an environment named **SECRET_DIR** is not set.
5. We can set it, by exporting the binary.

```
export SECRET_DIR=/root
```

> RESULT

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/15e82e97-598e-4cf6-97c2-8dd6d563d22c)


6. Great! It worked. Let's modify the env value to cat the file inside /root directory.
7. However, we got another problem here. Seems **cat** binary is marked not exist somehow.

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/dd2e1b5a-f43c-419a-9e6a-862723b7647c)


8. Kinda lucky for this chall I guess, I combined **ls** with **cat** and it's resulting to output the flag.
9. Maybe combining commands with pipeline somehoew changed how the shell interpreted.

```
export SECRET_DIR="ls -lh /root | cat /root/f*"
```

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/d1949e28-0229-45ae-81a1-e34f586aee2b)


10. Got the flag!
    
## FLAG:

```
picoCTF{Power_t0_man!pul4t3_3nv_19a6873b}
```
