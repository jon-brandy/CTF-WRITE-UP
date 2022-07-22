# extensions
#### Write-up author: [jon-brandy]()
## DESCRIPTION:
This is a really weird text file TXT? Can you find the flag?
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

