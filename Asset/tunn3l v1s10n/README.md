# tunn3l v1s10n
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
We found this [file](https://github.com/jon-brandy/CTF-WRITE-UP/blob/93f0b6a577105be65d1b1ce6f92fad75005849bb/Asset/tunn3l%20v1s10n/tunn3l_v1s10n). Recover the flag.
## HINT:
1. Weird that it won't display right...
## STEPS:
1. First download the file given.
2. Next, try to check what the file type is by run this command at your kali linux terminal:

```
file tunn3l_v1s10n
```

![image](https://user-images.githubusercontent.com/70703371/178663025-d7f5ab32-a87a-4ac5-93a4-a82787ef8ac3.png)

3. Since we got no clue, next try to see the intended file type by using hex editor.
4. Run this command at your kali linux terminal:

```
hexeditor tunn3l_v1s10n
```

![image](https://user-images.githubusercontent.com/70703371/178663284-9a41d0a4-c43c-483b-bd48-993f23eed434.png)

5. If you see at the top, there's two character -> `BM`. Which tells us it's a `BMP` file.
6. Then, let's change the file extension to `.bmp`.
7. 
