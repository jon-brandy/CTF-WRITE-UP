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


