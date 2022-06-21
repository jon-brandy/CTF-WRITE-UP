# Redaction gone wrong
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Now you DON’T see me. 
This [report](https://github.com/jon-brandy/CTF-WRITE-UP/blob/65ab1c1591872ed5cc074ad4cf1c1fe8f5a97413/Asset/Redaction%20gone%20wrong/Financial_Report_for_ABC_Labs.pdf) has some critical data in it, some of which have been redacted correctly, while some were not. 
Can you find an important key that was not redacted properly?
## HINT:
1. How can you be sure of the redaction?
## STEPS:
1. First, download the file given.
2. Based on the clue given, the flag is confirmed to be text covered in black.
3. If you search the internet, there are actually many ways you can do to get black-covered text. But the method I use is one of the easiest.
4. Just copy the whole text inside the document then paste it at the notepad.

![Screenshot (465)](https://user-images.githubusercontent.com/70703371/174810159-e7e6604e-fe03-4667-aee7-b8695b817589.png)

5. Finally we can see the flag!


--- 
## FLAG
```
picoCTF{C4n_Y0u_S33_m3_fully}
```
