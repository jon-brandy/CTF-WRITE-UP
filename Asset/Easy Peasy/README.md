# Easy Peasy
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
A one-time pad is unbreakable, but can you manage to recover the flag? 
(Wrap with picoCTF{}) `nc mercury.picoctf.net 11188` [otp.py](https://github.com/jon-brandy/CTF-WRITE-UP/blob/fee9da0a6e797eaaa7902bc0dc645396ca97a3b7/Asset/Easy%20Peasy/otp.py)
## HINT:
1. Maybe there's a way to make this a 2x pad.
## STEPS:
1. First download the python file given.

> CODE

```py
#!/usr/bin/python3 -u
import os.path

KEY_FILE = "key"
KEY_LEN = 50000
FLAG_FILE = "flag"


def startup(key_location):
	flag = open(FLAG_FILE).read()
	kf = open(KEY_FILE, "rb").read()

	start = key_location
	stop = key_location + len(flag)

	key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
	print("This is the encrypted flag!\n{}\n".format("".join(result)))

	return key_location

def encrypt(key_location):
	ui = input("What data would you like to encrypt? ").rstrip()
	if len(ui) == 0 or len(ui) > KEY_LEN:
		return -1

	start = key_location
	stop = key_location + len(ui)

	kf = open(KEY_FILE, "rb").read()

	if stop >= KEY_LEN:
		stop = stop % KEY_LEN
		key = kf[start:] + kf[:stop]
	else:
		key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

	print("Here ya go!\n{}\n".format("".join(result)))

	return key_location


print("******************Welcome to our OTP implementation!******************")
c = startup(0)
while c >= 0:
	c = encrypt(c)

```

2. Next, run the netcat command -> `nc mercury.picoctf.net 11188`.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/181180236-82f6dce1-6452-4078-b23d-49d358674e24.png)

3. Now, if you enter any random character to encrypt, it will always give you 32 bytes encrypted flag.

![image](https://user-images.githubusercontent.com/70703371/181182664-8f37a5ce-68c8-402c-b858-c2749bd6d358.png)

4. vrv


## REFERENCES
```
https://en.wikibooks.org/wiki/Cryptography/One_time_pads
```
