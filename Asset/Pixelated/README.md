# Pixelated
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
I have these 2 images, can you make a flag out of them? 
[scrambled1.png](https://github.com/jon-brandy/CTF-WRITE-UP/blob/89d64a98268824fc46fa3cdbea0bf3389d660d60/Asset/Pixelated/scrambled1.png) [scrambled2.png](https://github.com/jon-brandy/CTF-WRITE-UP/blob/89d64a98268824fc46fa3cdbea0bf3389d660d60/Asset/Pixelated/scrambled2.png)
## HINTS:
1. https://en.wikipedia.org/wiki/Visual_cryptography
2. Think of different ways you can "stack" images
## STEPS:
1. First, download both images given.
2. Next open the `.png` file to see it is corrupted or not.

> SCRAMBLED1.PNG

![image](https://user-images.githubusercontent.com/70703371/187844734-53a40f9e-8f2d-4f87-a945-ae395faea5fe.png)

> SCRAMBLED2.PNG

![image](https://user-images.githubusercontent.com/70703371/187844684-b078c7da-80dc-40ca-bfdc-ac895a0483c9.png)

3. Based from the hint number one, we may have to concate the images into one pieces.

![image](https://user-images.githubusercontent.com/70703371/187845038-03650698-651f-470d-8aaf-e5463fa1b90f.png)

4. For this solution i used a tools called **stegsolve.jar**.
5. Open the first image file.

![image](https://user-images.githubusercontent.com/70703371/187845545-298250fb-ff8a-49b9-8f1a-82fca668c2b2.png)

6. Then on the analyze tab, choose `image combiner`.

![image](https://user-images.githubusercontent.com/70703371/187845640-7923ab8f-6e30-4dc5-89a0-712db8ba2a03.png)

7. Choose the 2nd image.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/187845727-9119e246-0b8e-4e95-ae4d-1b71cdfdbe90.png)

8. Press the `>` button until `ADD`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/187845891-1a9f97a2-d47d-45a5-8f80-9c0818d3b7be.png)

9. Finally we got the flag!

## FLAG

```
picoCTF{d562333d}
```
