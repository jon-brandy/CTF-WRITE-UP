# PW Crack 5
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Can you crack the password to get the flag? 
Download the password checker [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/e3c973166d9c560e0d30662a42b69f4baded6c2e/Asset/PW%20Crack%205/level5.py) and you'll need the encrypted [flag](https://github.com/jon-brandy/CTF-WRITE-UP/blob/e3c973166d9c560e0d30662a42b69f4baded6c2e/Asset/PW%20Crack%205/level5.flag.txt.enc) and the [hash](https://github.com/jon-brandy/CTF-WRITE-UP/blob/e3c973166d9c560e0d30662a42b69f4baded6c2e/Asset/PW%20Crack%205/level5.hash.bin) in the same directory too. 
Here's a [dictionary](https://github.com/jon-brandy/CTF-WRITE-UP/blob/e3c973166d9c560e0d30662a42b69f4baded6c2e/Asset/PW%20Crack%205/dictionary.txt) with all possible passwords based on the password conventions we've seen so far.
## HINTS:
1. Opening a file in Python is crucial to using the provided dictionary.
2. You may need to trim the whitespace from the dictionary word before hashing. Look up the Python string function, `strip`.
3. The `str_xor` function does not need to be reverse engineered for this challenge.
## STEPS:
1. First, download all the files given in the same directory.
2. Then open the python code.

```py
import hashlib

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

flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_5_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")



level_5_pw_check()
```

3. I think it's similiar to challenge `PW Crack 4` but this time we are using a `.txt` file as password list.
4. Since it has `thousands` lines and strings, based from the hint number 2, we should use `strip()` function.
5. So i modified the python script:

```py
import hashlib

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

flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_5_pw_check():
    user_pw = open('dictionary.txt', 'r')
    for i in user_pw:
        index = i.strip("\n")
        user_pw_hash = hash_pw(index)
    
        if( user_pw_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), index)
            print(decryption)
            return
    print("That password is incorrect")



level_5_pw_check()


```

6. Next, try to run `python3 level5.py` at your kali linux terminal.

> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/181878791-97114056-2dd6-4356-825c-a627daa1d1a4.png)

7. Finally we got the file!

---

## FLAG

```
picoCTF{h45h_sl1ng1ng_40f26f81}
```



