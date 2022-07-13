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
7. Since the file is still corrupted. Open the hexeditor again or HxD and change this offset:

![image](https://user-images.githubusercontent.com/70703371/178680898-d695ffd7-6c0d-4249-b5e2-28db936fcf1d.png)

![image](https://user-images.githubusercontent.com/70703371/178681120-61a87d9b-5288-464a-a1b4-8fe727535944.png)

8. Finally we can open the image!

![image](https://user-images.githubusercontent.com/70703371/178681455-1db8337a-417a-4ba1-bdd2-bef3aa3f1d6f.png)

9. It says no flag.
10. Based from the hint, maybe we should change the pixels (?)
11. From [wikipedia](https://en.wikipedia.org/wiki/BMP_file_format), we should change the offset 0016h to change the image height.

![image](https://user-images.githubusercontent.com/70703371/178682582-eb19ecae-3f4e-424c-a2f7-e986bba2d873.png)

12. I changed it to 99.

![image](https://user-images.githubusercontent.com/70703371/178682955-d4a55353-9907-4d20-b47a-3c691ef07c6b.png)

13. I still got nothing.

![image](https://user-images.githubusercontent.com/70703371/178683019-73482e03-7bae-4e87-bbeb-799c46fd5967.png)

14. Next, i try to change the 00h17 value to 03 and the 00h16 value to 40.
15. Finally we got the flag!

![image](https://user-images.githubusercontent.com/70703371/178683926-839d1137-e1f2-4f66-9235-fdb25ebd6e37.png)

---

## FLAG:

```
picoCTF{qu1t3_a_v13w_2020}
```

**NOTES**:
```
I failed to solve it by myself due to lack of understanding of bitmap. 
Big thanks to -> Mr.Carliste | github -> https://github.com/carlislemc
```

## REFERENCES:

```
https://en.wikipedia.org/wiki/BMP_file_format
https://www.youtube.com/watch?v=X4kJiQdDn7M
```
