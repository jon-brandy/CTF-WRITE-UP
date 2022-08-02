# Operation Oni
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Download this disk image, find the key and log into the remote machine.
Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
- [Download disk image]()
- Remote machine: `ssh -i key_file -p 54121 ctf-player@saturn.picoctf.net`
## HINT:
- NONE
## STEPS:
1. First, download the disk file given.
2. Since it's a `.gz` file, unzip it by run -> `gunzip disk.img`.
3. Then i run `mmls disk.img`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182285628-524bd9e4-2762-4260-8799-5d5c6d250268.png)

4. Based from the output we got, let's se the last partition file by run -> `fls -o 206848 disk.img`.

![image](https://user-images.githubusercontent.com/70703371/182288253-207f5fee-827d-4d5e-919e-1cdd53bce1c3.png)

5. I think we can run the same steps as `Operation Orchid` challenge.
6. Run `binwalk -e disk.img` to extract every hidden file inside.
7. Open the extracted folder.

![image](https://user-images.githubusercontent.com/70703371/182285733-7688da31-a210-45b4-96fb-08bab302363a.png)

7. Go to `ext-root-0` folder.

![image](https://user-images.githubusercontent.com/70703371/182285814-dd966419-823b-4b14-8c20-87bb59028a59.png)

8. Go to `root` folder.
9. When i run `ls` seems the folder is empty.

![image](https://user-images.githubusercontent.com/70703371/182285922-6e40cd05-b310-4771-96d6-e17a4652a07a.png)

10. But we can run `ls -a` which will list every hidden file or folder inside the current directory.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182285994-4ccee732-7d76-40d8-914f-514c44f90e29.png)

11. We got one folder and one file.
12. Let's open the `.ash_history` file first. Run the `strings` command.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182286203-f5adbc00-51a4-4651-9a57-bd8920d6183b.png)

13. Seems it's just a ssh payload.
14. Now let's check the `.ssh`folder.

![image](https://user-images.githubusercontent.com/70703371/182286301-93c391a1-7c2e-444c-9f28-29b66f3a93a0.png)

15. The first file is the private key and the `.pub` file is the public key.

![image](https://user-images.githubusercontent.com/70703371/182286402-28e3d899-f941-4c53-a94c-e31c16d6b6fd.png)

![image](https://user-images.githubusercontent.com/70703371/182286423-d78fe840-5c5d-452f-aabe-5e77e8eca96a.png)

16. Let's copy the private key value to a file named `pvt_key` and run the `ssh` command.

![image](https://user-images.githubusercontent.com/70703371/182291604-29060d2d-d505-43d1-9ef8-6bb63f49ea33.png)

18. Forgot to make it NOT accesible by others, simply run -> `chmod 400 pvt_key` at super user mode `sudo su`.

> RESEARCH LINK

```
https://www.linuxtopia.org/online_books/introduction_to_linux/linux_The_chmod_command.html
```

19. Now run the `ssh` command again.
20. `ssh -i pvt_key -p 54121 ctf-player@saturn.picoctf.net`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182292689-92a3940c-f059-47e2-8349-c6976812244b.png)

20. Seems, i forgot to give an enter at the EOF.

![image](https://user-images.githubusercontent.com/70703371/182292783-c32da856-883a-4420-a196-77f77009c544.png)

21. Now save it with another file named `pvtKey`, then run `chmod 400 pvtKey` and run `ssh` again.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182292995-88fdb445-ab6d-41a8-8585-e3b568d0cbfc.png)

22. Next, try to run `ls`.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/182293054-523d849f-58db-4c53-b0af-c4dc49e9e7c7.png)

23. i Think this might be the flag, run the `strings` command.
24. Finally we found the flag!

![image](https://user-images.githubusercontent.com/70703371/182293135-64a6a492-e908-45bb-a84b-78643b412509.png)


---

## FLAG

```
picoCTF{k3y_5l3u7h_339601ed}
```


## REFERENCES

```
https://www.linuxtopia.org/online_books/introduction_to_linux/linux_The_chmod_command.html
```

