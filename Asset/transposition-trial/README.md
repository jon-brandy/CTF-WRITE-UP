# transposition-trial
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! 
The first word seems to be three letters long, maybe you can use that to recover the rest of the message. 
Download the corrupted message [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/c06314069389fda00b304e1b2d08902056967201/Asset/transposition-trial/message.txt).
## HINT:
1. Split the message up into blocks of 3 and see how the first block is scrambled.
## STEPS:
1. First, download the file given.
2. Next, let's see what's inside the `.txt` file.

![image](https://user-images.githubusercontent.com/70703371/182869969-ad1399e4-a715-429f-b416-01b3ba39f405.png)

```
heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V9AAB1F8}7
```

3. Well it is the flag, but the flag is corrupted.
4. Based from the hint, we may split the message into blocks of 3 and see how the first block is scrambled.
5. Since i can't make the script, so i did it manually by check if the current characters of the block is the third one, then move it to the front.

> RESULT

```
The Flag is
```
