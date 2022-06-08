# unpackme.py
## DESCRIPTION:
Can you get the flag? 
Reverse engineer this [Python program](https://github.com/jon-brandy/CTF-WRITE-UP/blob/6c5d21d7562d854cdbabc5317b76658d8f52e1f2/Asset/unpackme.py/unpackme.flag.py).
## HINT:
None
## STEP:
1. Download the source code first.
```py
import base64
from cryptography.fernet import Fernet

payload = b'gAAAAABiMD09KmaS5E6AQNpRx1_qoXOBFpSny3kyhr8Dk_IEUu61Iu0TaSIf8RCyf1LJhKUFVKmOt2hfZzynRbZ_fSYYN_OLHTTIRZOJ6tedEaK6UlMSkYJhRjAU4PfeETD-8gDOA6DQ8eZrr47HJC-kbyi3Q5o3Ba28mutKCAkwrqt3gYOY9wp3dWYSWzP4Tc3NOYWfu-SJbW997AM8GA-APpGfFrf9f7h0VYcdKOKu4Vq9zjJwmTG2VXWFET-pkF5IxV3ZKhz36L5IvZy1dVZXqaMR96lovw=='

key_str = 'correctstaplecorrectstaplecorrec'
key_base64 = base64.b64encode(key_str.encode())
f = Fernet(key_base64)
plain = f.decrypt(payload)
exec(plain.decode())
```
2. Try to change the `exec` -> (dynamically execute code of python programs) from line 19 to `print`.
3. We change it to print, because we just want to see what's inside the `plain` variable.

![Screenshot (413)](https://user-images.githubusercontent.com/70703371/172574349-770ce13e-b471-4b84-bd04-a4f42cd5a217.png)

### PROGRAM OUTPUT:
```
pw = input('What\'s the password? ')      

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_85f5d0ac}')
else:
  print('That password is incorrect.')    

```

4. Finally we can see the flag!

---

## FLAG:
```
picoCTF{175_chr157m45_85f5d0ac}
```
