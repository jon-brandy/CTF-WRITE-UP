# la cifra de
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
I found this cipher in an old book. Can you figure out what it says? Connect with `nc jupiter.challenges.picoctf.org 58295`.
## HINTS:
1. There are tools that make this easy.
2. Perhaps looking at history will help
## STEPS:
1. Run the netcat command at your kali linux terminal.

> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/180729351-ed67c722-806e-4db2-8b5b-e2d63b4f2643.png)

2. It is known as the `vigenere cipher text` but this time we don't have the key.
3. For this solution i used this [online](https://www.guballa.de/vigenere-solver) tools, to decode `vigenere` cipher text without the key.
4. Simply, paste the encrypted text then press the `break` button.

![image](https://user-images.githubusercontent.com/70703371/180730095-f4838af6-f0c4-4562-bc0b-fb92acb8d153.png)

> RESULT:

```
It is interesting how in history people often receive credit for things they did not create

During the course of history, the Vigenère Cipher has been reinvented many times

It was falsely attributed to Blaise de Vigenère as it was originally described in 1553 by Giovan Battista Bellaso in his book La cifra del. Sig. Giovan Battista Bellaso 

For the implementation of this cipher a table is formed by sliding the lower half of an ordinary alphabet for an apparently random number of places with respect to the upper halfpicoCTF{b311a50_0r_v1gn3r3_c1ph3ra966878a}

The first well-documented description of a polyalphabetic cipher however, was made around 1467 by Leon Battista Alberti.

The Vigenère Cipher is therefore sometimes called the Alberti Disc or Alberti Cipher.

In 1508, Johannes Trithemius invented the so-called tabula recta (a matrix of shifted alphabets) that would later be a critical component of the Vigenère Cipher.

Bellaso’s second booklet appeared in 1555 as a continuation of the first. The lower halves of the alphabets are now shifted regularly, but the alphabets and the index letters are mixed by means of a mnemonic key phrase, which can be different with each correspondent.
```

4. Finally we got the flag!

---

## FLAG

```
picoCTF{b311a50_0r_v1gn3r3_c1ph3ra966878a}
```
