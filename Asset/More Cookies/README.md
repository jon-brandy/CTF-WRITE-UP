# More Cookies
## DESCRIPTION:
I forgot Cookies can Be modified Client-side, 
so now I decided to encrypt them! http://mercury.picoctf.net:43275/
## HINTS:
1. https://en.wikipedia.org/wiki/Homomorphic_encryption
2. The search endpoint is only helpful for telling you if you are admin or not, you won't be able to guess the flag name
## STEPS:
1. First, open the website given.
2. Now open `inspect element` then choose the `application` tab and you can see there's a cookie called `auth_name` with the value as:

![image](https://user-images.githubusercontent.com/70703371/187207539-0983cc21-58ab-498b-95e7-a7a002ff2fe6.png)

> auth_name


![image](https://user-images.githubusercontent.com/70703371/187207615-26b4dcad-d5b5-4a3f-9835-ef9b81f2abfb.png)


```
eUszMGZMQkwxMGpOcjJJNkg3aUR3cnhzZThBZitqd3dDcFluOXdQZGoyZFJxUlliY2ZNK1V3STNweHNhQnZxWmRGUS9SSElqTnJWZjJDK3NWNmt4bzV6blB0UzFkaGIwZWFYSHY0U2dZbXBoei9OTUlzR1kzNXI2SXNyTDJHbmg=
```

3. Since the cookie's value is a `base64` text, let's decode it with this python code:

```python
import base64
import os

os.system('clear')
strings = 'eUszMGZMQkwxMGpOcjJJNkg3aUR3cnhzZThBZitqd3dDcFluOXdQZGoyZFJxUlliY2ZNK1V3STNweHNhQnZxWmRGUS9SSElqTnJWZjJDK3NWNmt4bzV6blB0UzFkaGIwZWFYSHY0U2dZbXBoei9OTUlzR1kzNXI2SXNyTDJHbmg='
base64_bytes = strings.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
result = message_bytes.decode('ascii')

print(result)
```

4. It seems we got unidentified output.

![image](https://user-images.githubusercontent.com/70703371/187208223-abde1015-83bb-4a99-beab-0b7b43dbd061.png)

> THE OUTPUT:

```
yK30fLBL10jNr2I6H7iDwrxse8Af+jwwCpYn9wPdj2dRqRYbcfM+UwI3pxsaBvqZdFQ/RHIjNrVf2C+sV6kxo5znPtS1dhb0eaXHv4SgYmphz/NMIsGY35r6IsrL2Gnh
```

5. Based from the hint number 1, i notice that we don't have to decrypt the text to find the flag, but we may perform operations on an encrypted text to find the flag.
6. What comes to my mind it **bit-flipping**.

> NOTES

![image](https://user-images.githubusercontent.com/70703371/187209124-fab4599c-b8dc-4cea-b73f-53ce423ef41d.png)

7. Notice at the description, the letter `C` , and `B` are capitalized.
8. Which gave us a clue that we may have to use `CBC bit-flip` attack to the encrypted text.
9. Hence, i made this script:

```py

```
6. Homomorphic encryption allows you to perform operations on encrypted text. 




