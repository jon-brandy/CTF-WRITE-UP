# patchme.py
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Can you get the flag? 
Run this [Python program](https://github.com/jon-brandy/CTF-WRITE-UP/blob/1f51cc14bfed6189105a338961ca86922fb090ed/Asset/patchme.py/patchme.flag.py) in the same directory as this [encrypted flag](https://github.com/jon-brandy/CTF-WRITE-UP/blob/1f51cc14bfed6189105a338961ca86922fb090ed/Asset/patchme.py/flag.txt.enc).
## HINT:
- NONE
## STEPS:
1. Download all the files given.
2. Open the python source code and change the `==` characters to `!=` at line 19.

![Screenshot (469)](https://user-images.githubusercontent.com/70703371/175041104-42eff94f-c6c5-4caf-8ab2-5056b195a7f3.png)

```python
### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('flag.txt.enc', 'rb').read()

def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw != "ak98" + \
                   "-=90" + \
                   "adfjhgj321" + \
                   "sleuth9000"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")



level_1_pw_check()

```

3. Now, run the source code in the same directory as the encrypted flag text file.
4. When the program asks for input, type `aaaa` then press enter.

![Screenshot (473)](https://user-images.githubusercontent.com/70703371/175050096-18c495a5-6c1d-4c19-8e14-081706971bcd.png)

5. Because we change the "if statements" algorithm by giving a flag if the input does not match what it should be, it is certain that the program will give an output that is a decrypted flag.

![Screenshot (472)](https://user-images.githubusercontent.com/70703371/175049788-07c9be06-6d02-4187-9357-91b433594cf2.png)

6. Finally, we got the flag!


---
## FLAG
```
picoCTF{p47ch1ng_l1f3_h4ck_21d62e33}
```
