# extensions
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
This is a really weird text file [TXT](https://github.com/jon-brandy/CTF-WRITE-UP/blob/81e72a25a0ff78e9c112061944c02713bcbb1601/Asset/extensions/flag.txt)? Can you find the flag?
## HINTS:
1. How do operating systems know what kind of file it is? (It's not just the ending!
2. Make sure to submit the flag as picoCTF{XXXXX}
## STEPS:
1. First, download the file given.
2. Next based from the hint number 1, let's check the file type by run this command:

```
file flag.txt
```

![image](https://user-images.githubusercontent.com/70703371/180366492-3451df06-5542-442a-a9ea-9dae412091d7.png)

3. Since it's a `PNG` file, let's convert it by run:

```
convert flag.txt flag.png
```

4. Now, let's open the image file.

![image](https://user-images.githubusercontent.com/70703371/180367173-08f1ef49-f5b7-4f3f-98a3-061679938664.png)

5. Finally we got the flag!

---
## FLAG

```
picoCTF{now_you_know_about_extensions}
```
