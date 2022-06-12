# Python Wrangling
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## Hints:
1. Get the Python script accessible in your shell by entering the following command in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/5c4c0cbfbc149f3b0fc55c26f36ee707/ende.py`.
2. `$ man python`

## Steps:
1. First, download the all 3 files by pressing the underlined text from the challenge. The 3 files consist of:
- ende.py
- flag.txt.en
- pw.txt

2. Next, try to check `flag.txt.en` file type is.

![Screenshot (334)](https://user-images.githubusercontent.com/98648342/169470247-e4f58e48-fa34-4913-80a6-77ff0cf2df13.png)

3. From the output we know that the file type is ASCII Text. Then try to run the python source code using this command `python3 ende.py`.

![Screenshot (335)](https://user-images.githubusercontent.com/98648342/169470479-6d06055d-7302-4792-a5ea-74ef8c7a0238.png)

4. The output tell us how to use the file properly. `-d` means decode and `-e` means encode.
5. Next try to see what's inside the `pw.txt` , using this command `cat pw.txt`.

![Screenshot (336)](https://user-images.githubusercontent.com/98648342/169470804-aa07176f-1857-47d0-af75-1d8b21a177f4.png)

6. Right now, we absolutely sure that the plaintext inside `pw.txt` is the password that might be the program prompted when we run the program.
7. After that let's run the python program using the guide they want us to. Run this command `python3 ende.py -d flag.txt.en` , means we want the program to decode the ciphertext inside the `flag.txt.en`

![Screenshot (338)](https://user-images.githubusercontent.com/98648342/169471472-e419391c-baa6-475c-86ab-f341b53b8e1f.png)

8. Enter the password using the plain text we got from `pw.txt`.
9. And finally we can see the flag!

![Screenshot (339)](https://user-images.githubusercontent.com/98648342/169471637-86f2cd9a-7204-4521-bc6d-0d9fa683869d.png)



---

## FLAG:
```
picoCTF{4p0110_1n_7h3_h0us3_192ee2db}
```
