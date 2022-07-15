# Disk, disk, sleuth!
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Use `srch_strings` from the sleuthkit and some terminal-fu 
to find a flag in this disk image: [dds1-alpine.flag.img.gz]()
## HINTS:
1. Have you ever used `file` to determine what a file was?
2. Relevant terminal-fu in picoGym: https://play.picoctf.org/practice/challenge/85
3. Mastering this terminal-fu would enable you to find the flag in a single command: https://play.picoctf.org/practice/challenge/48
4. Using your own computer, you could use qemu to boot from this disk!
## STEPS:
1. First, download the zip file given.
2. Next, based from the hint, let's try `file dds1-alpine.flag.img.gz` to check the file extension is right or not.

![image](https://user-images.githubusercontent.com/70703371/179222200-ce72969a-5aa9-4981-b1df-ac7e291a0565.png)

> TO UNZIP `.gz` FILE EXTENSION , RUN `gzip -d [FILE_NAME]`. `-d` means `decode`.

3. Since it's right, let's unzip it by run this command -> `gzip -d dds1-alpine.flag.img.gz`.
4. Then, let's try run `strings dds1-alpine.flag.img | grep 'pico'` to check are there any `pico` strings.

![image](https://user-images.githubusercontent.com/70703371/179222765-a655728b-c84c-4982-9135-19a431b5afc5.png)

5. Finally we found the flag!

---
## FLAG

```
picoCTF{f0r3ns1c4t0r_n30phyt3_564ff1a0}
```

