# Wave a flag
## Hints:
1. This program will only work in the webshell or another linux computer.
2. To get the file accessible in your shell, enter the following in the Terminal prompt: 
`$ wget https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm`.
3. Run this program by entering the following in the Terminal prompt: `$ ./warm`, but you'll first have to make it executable with 
`$ chmod +x warm`.
4. `-h` and `--help` are the most common arguments to give to programs to get more information from them!
5.  Not every program implements help features like -h and --help.

## Steps:
1. First, download the file using this command `wget https://mercury.picoctf.net/static/beec4f433e5ee5bfcd71bba8d5863faf/warm`.
2. After that, make the program executable with this command `chmod +x warm`.
3. Third, run `./warm`.
4. Finally, we just have to run `./warm -h` and we got the flag!
---
![pict](https://github.com/jon-shel/CTF-WRITE-UP/blob/134932d731008a07f16effb40df0ab1c85f14d32/Asset/Wave%20a%20flag/Screenshot%20(331).png)


---

## FLAG
```
picoCTF{b1scu1ts_4nd_gr4vy_616f7182}
```
