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

3. Next, open your kali linux terminal..
