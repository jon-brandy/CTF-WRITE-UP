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

![WhatsApp Image 2022-07-22 at 10 15 23 AM](https://user-images.githubusercontent.com/70703371/180355226-3fb64248-d9a2-485c-a0f2-34d5134d00e0.jpeg)

6. This header PNG is broken, the value should be PNG. So we need to change the value.

![image](https://user-images.githubusercontent.com/70703371/180355734-f1c80438-a897-4084-a1ef-2f7cfb6ad2e4.png)

7. For this solution, i downloaded any PNG image, then i opened it using the HxD.
8. For example i download [this](https://github.com/jon-brandy/CTF-WRITE-UP/blob/60f23e5255d0501b43696f31fd1aa263be0144f4/Asset/advanced-potion-making/Logo-Binus-University-Universitas-Bina-Nusantara-Original-PNG.png) iamge. Then i opened it on HxD.

![image](https://user-images.githubusercontent.com/70703371/180356703-4d3094d1-7149-47df-a975-36e3b4c59955.png)

9. It seems there's 8 different bits. Let's copy the value and paste it on the challenge file.

![image](https://user-images.githubusercontent.com/70703371/180356893-786c9d06-b0e5-4c68-9764-0c016edf5111.png)

10. Then press `ctrl + s`.
11. Now open the image file.

![image](https://user-images.githubusercontent.com/70703371/180357149-f0eb97cd-f6ac-4488-a5db-ebd7b7d614cf.png)

12. Hmm.. We got nothing.
13. This reminds me of `steganography`. So i tried to use `stegsolve.jar`

![image](https://user-images.githubusercontent.com/70703371/180360217-12ce743c-3ece-46ad-b8e7-5a9314f8d1da.png)

14. Press the `right` button if you still can't see the flag.

![image](https://user-images.githubusercontent.com/70703371/180360001-9496f404-e8c5-441d-9cc8-7e17a22e518f.png)

15. Finally, at the red plane 0, we got the flag!

![image](https://user-images.githubusercontent.com/70703371/180360285-a1f49109-c4e4-45d6-9d4d-1cf0b7cee056.png)


---
## FLAG

```
picoCTF{w1z4rdry}
```
