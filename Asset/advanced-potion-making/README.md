# advanced-potion-making
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it! 
```
CHALLENGE ENDPOINTS
```
[download](https://github.com/jon-brandy/CTF-WRITE-UP/blob/df1caf301eb0452ea593a0258b731f2631c61fdc/Asset/advanced-potion-making/advanced-potion-making)
## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Next i tried to see what does the file type by run `file` command.

![image](https://user-images.githubusercontent.com/70703371/179985299-a9197fde-04ac-43a3-80de-0a3710a7215a.png)

3. Since we got no clue and based from the description, since it's a corrupted file.
4. We can fix it by change the `hex` value. let's open it using `hexeditor`. For this solution i used `HxD` at windows.

![image](https://user-images.githubusercontent.com/70703371/179985451-368b952d-c8f7-410c-aa77-4df76aba34cc.png)

5. If you pay attention to the header. This file seems to have PNG characters

![WhatsApp Image 2022-07-22 at 10 12 30 AM](https://user-images.githubusercontent.com/70703371/180355048-3e50bc1e-77ae-4bfb-bbf7-1e26c17ddbdf.jpeg)

6. 
