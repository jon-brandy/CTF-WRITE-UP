# Tapping
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Theres tapping coming in from the wires. What's it saying `nc jupiter.challenges.picoctf.org 9422`.
## HINTS:
1. What kind of encoding uses dashes and dots?
2. The flag is in the format PICOCTF{}
## STEPS:
1. First, run the netcat command at your kali linux terminal.

![image](https://user-images.githubusercontent.com/70703371/180732442-860e0f37-eb02-4245-82f8-4f0894f56491.png)

```
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ..--- -.... ---.. ...-- ---.. ..--- ....- -.... .---- ----- }
```

2. Well, we can simply guess it is a morse code.
3. For this solution, i used this online [tool](https://morsecode.world/international/translator.html)
4. Paste the morse code but remove the curly bracket first.

> OUTPUT:

```
PICOCTFM0RS3C0D31SFUN2683824610
```

5. Now, put the curly brackets again and we have the complete flag now!


---

## FLAG

```
picoCTF{M0RS3C0D31SFUN2683824610}
```
