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
7. 
