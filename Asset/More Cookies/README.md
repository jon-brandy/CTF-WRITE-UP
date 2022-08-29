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
from base64 import *
import os

os.system('clear')
strings = 'eUszMGZMQkwxMGpOcjJJNkg3aUR3cnhzZThBZitqd3dDcFluOXdQZGoyZFJxUlliY2ZNK1V3STNweHNhQnZxWmRGUS9SSElqTnJWZjJDK3NWNmt4bzV6blB0UzFkaGIwZWFYSHY0U2dZbXBoei9OTUlzR1kzNXI2SXNyTDJHbmg='
result = b64decode(strings)

print(result)
```

4. It seems we got unidentified output.

![image](https://user-images.githubusercontent.com/70703371/187216654-64a30cab-478f-45fa-9b5c-7ea9bf6cd672.png)

> THE OUTPUT:

```
yK30fLBL10jNr2I6H7iDwrxse8Af+jwwCpYn9wPdj2dRqRYbcfM+UwI3pxsaBvqZdFQ/RHIjNrVf2C+sV6kxo5znPtS1dhb0eaXHv4SgYmphz/NMIsGY35r6IsrL2Gnh
```

5. Well i tried to decode it once more and we still got unidentified output.

> THE OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/187216771-8fbfd16d-ed80-40f8-b5b8-19bc92bfc263.png)


6. Based from the hint number 1, i notice that we don't have to decrypt the text to find the flag, but we may perform operations on an encrypted text to find the flag.
7. What comes to my mind it **bit-flipping**.

> NOTES

![image](https://user-images.githubusercontent.com/70703371/187209124-fab4599c-b8dc-4cea-b73f-53ce423ef41d.png)

8. Notice at the description, the letter `C` , and `B` are capitalized.

![image](https://user-images.githubusercontent.com/70703371/187211319-f68e2de5-294c-4d40-b64a-13f940c7fb1b.png)

9. Which gave us a clue that we may have to use `CBC bit-flip` attack to the encrypted text.
10. Hence, i used this python script, i found from the internet from -> `https://github.com/HHousen`.

```py
import requests
from base64 import *
from tqdm import tqdm
import os

os.system('clear')

nc = "http://mercury.picoctf.net:43275/"

sh = requests.Session()
sh.get(nc)
cookie = sh.cookies["auth_name"]
strings = b64decode(cookie)
strings2 = b64decode(strings)


def exploit():
    for position_idx in tqdm(range(0, len(strings2))):
        for bit_idx in range(0, 8):
            bitflip_guess = (
                strings2[0:position_idx]
                + ((strings2[position_idx] ^ (1 << bit_idx)).to_bytes(1, "big"))
                + strings2[position_idx + 1 :]
            )

            guess = b64encode(b64encode(bitflip_guess)).decode()
            sh = requests.get(nc, cookies={"auth_name": guess})
            if "picoCTF" in sh.text:
                print("Flag: " + sh.text.split("<code>")[1].split("</code>")[0])
                return

exploit()
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/187219065-d70e2f21-8b4a-47d1-bfdf-d19044db02c6.png)


## FLAG

```
picoCTF{cO0ki3s_yum_1b75d657}
```


## REFERENCES:

```
https://crypto.stackexchange.com/questions/66085/bit-flipping-attack-on-cbc-mode/66086#66086
https://www.youtube.com/watch?v=Fs3EbH-Wdhc
```


