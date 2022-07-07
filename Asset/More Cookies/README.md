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

```
M21aOS9xUW0yZHBRTFdPNXp4Ym40QnREaG1jaUlOaXpieVJ4cFdMd0Qvb2VveGpmRzBOMyt6MFpkVG1YbW1KWkZRdnljV1czWWgwWC9zK2l0WjV6V3F1S05pVjRLcGY3R2d1OERRR3lxRnFNc0VVTTZlcHhCSG9LTWxhOVVTVUo=
```

![image](https://user-images.githubusercontent.com/70703371/177486447-fa34b030-a0bc-43b2-aae7-122b3243603c.png)

3. Since the cookie's value is a `base64` text, let's decode it with this python code:

```python
import base64
import os

os.system('cls')
strings = 'M21aOS9xUW0yZHBRTFdPNXp4Ym40QnREaG1jaUlOaXpieVJ4cFdMd0Qvb2VveGpmRzBOMyt6MFpkVG1YbW1KWkZRdnljV1czWWgwWC9zK2l0WjV6V3F1S05pVjRLcGY3R2d1OERRR3lxRnFNc0VVTTZlcHhCSG9LTWxhOVVTVUo='
base64_bytes = strings.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
result = message_bytes.decode('ascii')

print(result)
```

4. It seems the output are still in gibberish, we can conclude it still encrypted.

![image](https://user-images.githubusercontent.com/70703371/177780668-fb786ac5-cef5-4c57-8acd-279a57afe9a4.png)

> THE OUTPUT:

```
3mZ9/qQm2dpQLWO5zxbn4BtDhmciINizbyRxpWLwD/oeoxjfG0N3+z0ZdTmXmmJZFQvycWW3Yh0X/s+itZ5zWquKNiV4Kpf7Ggu8DQGyqFqMsEUM6epxBHoKMla9USUJ
```

5. Based from the hint number 1, i think it is a homomorphic cipher text.
6. Homomorphic encryption allows you to perform operations on encrypted text. 

**NOTES: 
```
I noticed that the letters "CBC" are oddly capitalized in the challenge description. So, It's a CBC bitflip. Meaning the encrypted text contains a bit that determines if it's admin or not, so probably something like `admin=0` and if we change the correct bit, then we can set `admin=1`. But I don't know it's position so I brute forced it with this python code:
```


