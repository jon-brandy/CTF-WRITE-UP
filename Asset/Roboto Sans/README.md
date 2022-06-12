# Roboto Sans
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
The flag is somewhere on this web application not necessarily on the website. Find it. Check [this](http://saturn.picoctf.net:64710/) out.
## HINT:
**NONE**
## STEPS:
1. If you are familiar with `where are the robots` challenge from picoCTF 2019, the solution is familiar.
2. Try to use `DIRB` from your kali linux and on your terminal type this command `dirb http://saturn.picoctf.net:64710/ -X .txt`. This might be take a few minutes.
3. As a reminder, `-X` means *execute*, so we want to search are there any files that contain the `.txt` extension.

![Screenshot (403)](https://user-images.githubusercontent.com/98648342/172106043-b33c0a53-337a-41ef-90b3-0548147e1cc1.png)

5. This result shows that there is a file called `robots.txt`. Now try to change the url to `http://saturn.picoctf.net:64710/robots.txt`.
6. And we get this result:

![Screenshot (401)](https://user-images.githubusercontent.com/98648342/172104246-8fd018de-0a1e-4b7e-9cc4-f2e8f4eeb5a0.png)

7. If you check carefully, we can conclude that there are some `base64` text.
8. Try to decode some of them using online decoder from [this](https://www.base64decode.org/) website or you can put the text into a `.txt` file and run this command
`base64 -d file.txt` on your linux terminal. Or if you don't want to put it into a `.txt` file, you can run this command `echo -n ZmxhZzEudHh0 | base64 -d`.
9. If we try to decode this `ZmxhZzEudHh0`, we get this `flag1.txt`. But if we try to decode the other one `anMvbXlmaWxlLnR4dA==`, we get this `js/myfile.txt`.
10. Now let's try to open the second one by changing the url to `http://saturn.picoctf.net:64710/js/myfile.txt`.
11. Finally, we can see the flag!

![Screenshot (402)](https://user-images.githubusercontent.com/98648342/172105805-64572927-b8d7-4fdb-913b-ba726b2d6e79.png)


---

## FLAG
```
picoCTF{Who_D03sN7_L1k5_90B0T5_032f1c2b}
```
