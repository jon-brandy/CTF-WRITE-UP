# Disk, disk, sleuth! II
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
All we know is the file with the flag is named `down-at-the-bottom.txt`... Disk image: [dds2-alpine.flag.img.gz]()
## HINTS:
1. The sleuthkit has some great tools for this challenge as well.
2. Sleuthkit docs here are so helpful: [TSK Tool Overview](http://wiki.sleuthkit.org/index.php?title=TSK_Tool_Overview)
3. This disk can also be booted with qemu!
## STEPS:
1. First, download the file given.
2. Next, unzip it by run `gzip -d dds2-alpine.flag.img.gz`
3. Then, i used the same method as the previous challenge, but i got nothing.

![image](https://user-images.githubusercontent.com/70703371/179225036-fe8ca708-c482-4a1d-97d6-1f85e06d38da.png)

4. Based from the hint number 3, let's install qemu by run this command -> `sudo apt-get install qemu-kvm`.
5. Next to boot up the images, run this command -> `qemu-system-x86_64 dds2-alpine.flag.img`

![image](https://user-images.githubusercontent.com/70703371/179229363-feb4150b-bc5a-4639-b8e9-2e5dab1ad83f.png)

6. Enter the username as `root` and the password as `root`.
7. After logged in, i run `ls` to see are there any directories or files.

![image](https://user-images.githubusercontent.com/70703371/179229929-21eabd08-9af9-47de-85a5-5234c22c0575.png)

8. Looks like there;s a file we've been looking for.
9. Run `cat down-at-the-bottom.txt` to see what's inside.

![image](https://user-images.githubusercontent.com/70703371/179230112-67a8ee6b-4474-44c9-987a-92be3a7898a5.png)

10. Finally we found the flag!


---
## FLAG
```
picoCTF{f0r3ns1c4t0r_n0u1c3_db59daa5}
```
