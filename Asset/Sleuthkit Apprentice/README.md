# Sleuthkit Apprentice
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Download this disk image and find the flag. Note: if you are using the webshell, 
download and extract the disk image into /tmp not your home directory.

- [Download compressed disk image]()
## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Next, since it's a `.gz` file, we can unzip it by run -> `gunzip disk.flag.img.gz` at your kali linux terminal.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/181508488-1d041825-f778-49bf-9d0b-5bc4a5e55c0e.png)

3. I tried to run `strings` but we got no clue.

![image](https://user-images.githubusercontent.com/70703371/181509235-e12492eb-cdc4-485c-90eb-1a1f2df47f0b.png)

4. For this solution, we may use `sleuthkit` which is an open source tool. But to keep it simple, i used `binwalk`.
5. Run `binwalk -e disk.flag.img`, to extract every hidden files inside.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/181515716-02ab6603-78b4-414b-9892-e8e9795dfb0e.png)

6. Go to the extracted folder, then go to `ext-root-0`.

![image](https://user-images.githubusercontent.com/70703371/181515836-04d99a59-b192-4401-8d09-e6ffb6fa7673.png)

7. Now go to `root`.

![image](https://user-images.githubusercontent.com/70703371/181515902-b8d900f8-9bcb-4788-838b-0355c9c3414a.png)

8. Go to `my_folder`.

![image](https://user-images.githubusercontent.com/70703371/181516019-a98ed09f-78bc-46b9-92bc-7070b3762170.png)

9. I think we got the flag.. Let's see what's inside using `strings`.

![image](https://user-images.githubusercontent.com/70703371/181516180-7dccd96e-0fa0-4aff-b81d-616bfbea8b4a.png)

10. Since, we got no output, check the file type.

![image](https://user-images.githubusercontent.com/70703371/181516272-6c8dfb83-17d8-4c56-885b-1460bd0e07aa.png)

11. Ok, now open hexeditor to see what's inside.

![image](https://user-images.githubusercontent.com/70703371/181516419-2ee3b718-c6ef-42ae-abeb-4200c0f8f3c2.png)

12. Finally we got the flag!

```
00000000  00 70 00 69  00 63 00 6F   00 43 00 54  00 46 00 7B                                                                                          .p.i.c.o.C.T.F.{
00000010  00 62 00 79  00 37 00 33   00 5F 00 35  00 75 00 72                                                                                          .b.y.7.3._.5.u.r
00000020  00 66 00 33  00 72 00 5F   00 32 00 66  00 32 00 32                                                                                          .f.3.r._.2.f.2.2
00000030  00 64 00 66  00 33 00 38   00 7D 00 0A                                                                                                       
.d.f.3.8.}..
```

---

## FLAG

```
picoCTF{by73_5urf3r_2f22df38}
```
