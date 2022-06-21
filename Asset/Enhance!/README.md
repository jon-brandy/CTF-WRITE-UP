# Enhance!
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Download this image file and find the flag.
[Download image file](https://github.com/jon-brandy/CTF-WRITE-UP/blob/36fbdbcc5edd0bc2f3a7705a26e912ffd13fda90/Asset/Enhance!/drawing.flag.svg)
## HINT:
- NONE
## STEPS:
1. First, download the given photo file.
2. Next, in your kali linux terminal type this command `cat drawing.flag.svg`, then press enter!

![Screenshot (453)](https://user-images.githubusercontent.com/70703371/174711031-635216ac-838a-4ee5-8941-6195953073ae.png)

3. Inside the `<text>` tag, if we look closely, we can see that there are several partitions of the flag.

![Screenshot (453)](https://user-images.githubusercontent.com/70703371/174711230-f8efc464-ff34-4da3-a67d-fc3163110a71.png)

4. Finally, we just have to concate all of them and we got the flag!


---

## FLAG
```
picoCTF{3nh4nc3d_d0a757bf}
```
