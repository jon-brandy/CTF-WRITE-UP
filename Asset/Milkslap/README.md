# Milkslap
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
[🥛](http://mercury.picoctf.net:48319/)
## HINT:
1. Look at the problem category
## STEPS:
1. First, open the website given.

![image](https://user-images.githubusercontent.com/70703371/180361257-96bec765-6ac0-4ed6-acf8-0239848e4bdf.png)

2. Now, let's open the source code file.
3. At the `.css` file, let's download the `concat_v.png` file.

![image](https://user-images.githubusercontent.com/70703371/180361581-402bb1d1-b073-4686-bd1b-3c8b625f9c8a.png)

4. Based from the hint, since it's a forensic challenge, it may be a `stegano` technique.
5. For this solution i used the `zsteg` tools.
6. At your kali linux terminal, run this command:

```
zsteg -v concat_v.png
```

7. Finally we got the flag!

![image](https://user-images.githubusercontent.com/70703371/180362012-8409cc99-a42a-428e-9a7c-1adf62002f30.png)


---
## FLAG

```
picoCTF{imag3_m4n1pul4t10n_sl4p5}
```
