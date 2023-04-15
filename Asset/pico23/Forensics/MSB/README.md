# MSB
> Write-up author: vreshco
## DESCRIPTION:
This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image... 
Download the image here
## HINT:
- What's causing the 'corruption' of the image?
## STEPS:
1. Given a corrupted "color" png file.

![image](https://user-images.githubusercontent.com/70703371/232224055-98501e16-e6f9-4f20-9215-74d429b5d299.png)


2. Based from the chall's title name, what comes to my mind, we shall extract the RGB values.

![image](https://user-images.githubusercontent.com/70703371/232224712-b367a0ae-8ab6-4e47-8725-e4ef62c01f9e.png)


3. Using **stegsolve** we can extract the hidden message in RGB values and saved it to a file.
4. Now let's find the flag prefixes.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/232225017-d7d53ffe-082e-4a03-a902-20f040dd7dd4.png)


5. There is the flag!
6. Let's open the file in vscode.

![image](https://user-images.githubusercontent.com/70703371/232225125-2746584a-9994-4b53-98f6-8d3ce3b5cca7.png)


7. Got the flag!

## FLAG

```
picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_ee3cb4d8}
```



