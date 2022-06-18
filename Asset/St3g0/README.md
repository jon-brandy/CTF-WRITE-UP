# St3g0
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Download this image and find the flag.
[Download image](https://github.com/jon-brandy/CTF-WRITE-UP/blob/276758d2df2b6a2d9d5eab59d6971f84ef1f60f0/Asset/St3g0/pico.flag.png)
## HINT:
1. We know the end sequence of the message will be $t3g0.
## STEPS:
1. The method I use is to use a tool called `zteg` on linux. But I think there are other, more efficient ways.
2. In kali linux terminal, type `zteg pico.flag.png`, then press enter.

![Screenshot (452)](https://user-images.githubusercontent.com/70703371/174425038-df77c8ae-0aa4-48ec-a4c3-56b7aab37ed2.png)

3. Finally, we got the flag!

---

## FLAG
```
picoCTF{7h3r3_15_n0_5p00n_a9a181eb}
```
