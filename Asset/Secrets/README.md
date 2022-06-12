# Secrets
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
We have several pages hidden. Can you find the one with the flag?
The website is running [here](http://saturn.picoctf.net:49917)
## HINTS:
1. folders folders folders
## STEPS:
1. Try to inspect the element and check all the source code first.

![Screenshot (391)](https://user-images.githubusercontent.com/98648342/172051341-d3a6e67e-eba8-4301-b880-58452e18e57d.png)

2. From the `index.html` file, we can guess that there is a folder called `secret`. So try to change the url to `http://saturn.picoctf.net:49917/secret/`.
3. Then, try to inspect the element again. We can see that there is a folder called `hidden`.

![Screenshot (395)](https://user-images.githubusercontent.com/98648342/172051454-9c6c6e05-04e0-4339-9139-149f1ce283af.png)

4. Now try to go to the `hidden` folder by change the URL to this  `http://saturn.picoctf.net:49917/secret/hidden/`.
5. Next, try to inspect the element again! And we can see that there is a folder called `superhidden`.

![Screenshot (396)](https://user-images.githubusercontent.com/98648342/172051594-ff5e373a-d32c-46ea-abf9-9c559bd29984.png)

6. Now try to go to the `superhidden` folder by change the URL to this `http://saturn.picoctf.net:49917/secret/hidden/superhidden/`

![Screenshot (397)](https://user-images.githubusercontent.com/98648342/172051678-2287ffac-b4a7-442b-9214-5adaca4fbbcb.png)

7. Finally, open the css file, and change the flag color to `black`.

![Screenshot (398)](https://user-images.githubusercontent.com/98648342/172051743-eb1a6499-2494-4959-a6ab-d09c04b41353.png)

---

## FLAG:
```
picoCTF{succ3ss_@h3n1c@10n_790d2615}
```
