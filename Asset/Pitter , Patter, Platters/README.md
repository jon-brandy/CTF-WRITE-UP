# Pitter , Patter , Platters
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
'Suspicious' is written all over this disk image. 
Download [suspicious.dd.sda1]()
## HINTS:
1. It may help to analyze this image in multiple ways: as a blob, and as an actual mounted disk.
2. Have you heard of slack space? There is a certain set of tools that now come with Ubuntu that I'd recommend for examining that disk space phenomenon...
## STEPS:
1. First download the disk given.
2. Next, check the file type first.

![image](https://user-images.githubusercontent.com/70703371/186068826-2dd34dca-ae57-4e5b-8372-338af4726c96.png)

3. It seems the file is not corrupted, so we may see the file system contents by run `fls` command.

> COMMAND

```
fls suspicious.dd.sda1
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/186069005-53982c74-c2cc-4239-922c-208b4aa5ba3b.png)

4. There's a file that caught my attention namely `suspicious-file.txt`.
5. Let's go there by run the `icat` command.

> COMMAND

```
icat suspicious.dd.sda1 12
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/186069278-4bf157f2-ed70-447e-a612-93f7c926cee5.png)

6. Well let's try to use an online tools called [Autopsy]().

