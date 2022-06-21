# Sleuthkit Intro
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Download the disk image and use `mmls` on it to find the size of the Linux partition. 
Connect to the remote checker service to check your answer and get the flag. 
Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
[Download disk image]()
Access checker program: `nc saturn.picoctf.net 52279`
## HINT:
- NONE
## STEPS:
1. Open your kali linux terminal.
2. Next, try to extract the `disk.img.gz` file first.
3. Then at your kali linux terminal, type command `mmls disk.img`.

![Screenshot (460)](https://user-images.githubusercontent.com/70703371/174725355-e3acba4b-48bb-4f8f-8d0e-c9f3efa0c25d.png)

4. Now type this command `nc saturn.picoctf.net 52279` at your kali linux terminal then press enter.

![Screenshot (461)](https://user-images.githubusercontent.com/70703371/174725878-8b24dc6e-3d33-4f3b-8db3-be09e2d7ff5b.png)

5. The length answer is `202752` based from the output from the `mmls disk.image` command.

![Screenshot (461)](https://user-images.githubusercontent.com/70703371/174725989-f5b5e071-a824-4ced-9485-03f0c95b9ec0.png)

6. Input the number, then press enter.
7. Finally we got the flag!

![Screenshot (462)](https://user-images.githubusercontent.com/70703371/174726165-b5315dbd-6fd8-4589-956c-97ae047e2f47.png)


---
## FLAG
```
picoCTF{mm15_f7w!}
```
