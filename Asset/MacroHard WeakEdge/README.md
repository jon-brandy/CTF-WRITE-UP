# MacroHard WeakEdge
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
I've hidden a flag in this file. 
Can you find it? [Forensics is fun.pptm](https://github.com/jon-brandy/CTF-WRITE-UP/blob/052c839f7cc979a15bc0992c5761785ca3eb89ed/Asset/MacroHard%20WeakEdge/Forensics%20is%20fun.pptm)
## HINTS:
- NONE
## STEPS:
1. First, download the file given.
2. Next, run this command at your kali linux terminal to see hidden files inside this file.

```
binwalk 'Forensics is fun.pptm'
```

![image](https://user-images.githubusercontent.com/70703371/178912081-9a1efdc6-7536-4889-a6bf-287701be3853.png)

![image](https://user-images.githubusercontent.com/70703371/178912251-05055c8d-395a-4274-a4d0-c18c101be00b.png)

3. Looks like it hides many files and there's one path that caught my attention:

![image](https://user-images.githubusercontent.com/70703371/179130007-56583da0-02a1-4d70-9314-1f4ec8c11aa5.png)

4. Now let's extract it by run this command:

```
binwalk -e 'Forensics is fun.pptm'
```

5. Open this folder:

![image](https://user-images.githubusercontent.com/70703371/179130109-193c7fb8-dc4c-4db3-8b1e-5e85ef6af491.png)

6. Next, 
