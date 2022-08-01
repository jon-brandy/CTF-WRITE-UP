# Operation Orchid
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
- [Download compressed disk image](https://artifacts.picoctf.net/c/238/disk.flag.img.gz)
## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Next, check the file type first by run `file disk.flag.img.gz`.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/182151554-4ca60849-443e-42cb-b653-f8ebc0a7b775.png)

**NOTES**: 

```
BASED FROM THE DESCRIPTION, UNZIP THE FILE INTO /tmp.
```

3. Now unzip the `.gz` file by run -> `gunzip disk.flag.img.gz`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182151830-27037413-10ff-46af-8cea-4b8424e8c625.png)

4. Then i run `file disk.flag.img` to see what's the file type again.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/182153268-8c79d0be-914e-4393-87dd-e114b5ed4ea6.png)

5. Based from that output we may use `qemu` by run this command -> `qemu-system-x86_64 disk.flag.img` to boot the disk.
6. But, since we don't have any clue about the username and the password, so it will be useless.
7. Next, i tried to extract all the hidden files inside the disk by run `binwalk -e disk.flag.img`.

> ![image](https://user-images.githubusercontent.com/70703371/182154285-e68333c9-0e56-4b92-8c2b-42b2075c768e.png)

8. Open the extracted folder.

![image](https://user-images.githubusercontent.com/70703371/182154381-e9804e6d-17b4-4926-ae80-3ed62d8e4a04.png)

9. Go to `ext-root-0`.

![image](https://user-images.githubusercontent.com/70703371/182154444-26ecad4a-fdac-4ebe-8e3b-5aded0f0ed53.png)

10. Go to the `root` folder.

![image](https://user-images.githubusercontent.com/70703371/182154494-3d7a151a-39ac-470d-bbe1-75d89c16997a.png)

11. We got this encoded flag.
12. I think there's might be another hidden file inside this folder.
13. To check that, i run `ls -a`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182154645-74d1a2a2-91ad-421a-98ae-36003e3ac7df.png)

14. Found it! Another file called `.ash_history`.
15. Check the file type first.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/182154825-8c7c5958-5253-4e42-a6c8-5c89111367a4.png)

16. Since, it's an `ASCII text` file, run this command -> `strings .ash_history`.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/182154994-ae49d805-f41a-4246-9624-359ced8bb947.png)

17. Seems, it's an instructions to decode the flag, let's follow it.
18. Run `touch flag.txt` to make flag.txt file.
19. Then we have to modify this command -> `openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567` in order to decode the flag and print the output to `flag.txt` file.

> THE COMMAND I MODIFIED

```
openssl aes256 -d -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182159451-2b5d31e9-12f2-441c-b940-12154ebe7129.png)


20. Now check the `flag.txt` file.

![image](https://user-images.githubusercontent.com/70703371/182159492-440751de-d619-4fbd-8d4f-9d1c852ededf.png)

21. Finally! We got the flag.


---

## FLAG

```
picoCTF{h4un71ng_p457_1d02081e}
```
