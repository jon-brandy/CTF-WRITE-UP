# What Lies Within
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
There's something in the [building]. Can you retrieve the flag?
## HINTS:
1. There is data encoded somewhere... there might be an online decoder.
## STEPS:
1. First, download the given file.
2. Next, based from the description,i conclude we may use `binwalk` command to find hidden file.
3. But i got nothing, then i think it might be a `steganography`, so i tried to use `zsteg` first to check are there hidden messages.

> COMMAND:

```
zsteg -v buildings.png
```

4. Finally we got the flag!

![image](https://user-images.githubusercontent.com/70703371/180368361-a4a5942e-fadf-453e-a6a4-3da272e56595.png)


---
## FLAG

```
picoCTF{h1d1ng_1n_th3_b1t5}
```
