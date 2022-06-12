# credstuff
## DESCRIPTION:
We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it?
Download the leak here.
The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.
## HINT:
-
## STEPS:
1. Open the website.
2. Inspect element and go to `Application tab > Cookies`.
3. Change the value of `name` to 18 **(for instant flag)**.
4. Wala, you get the flag!

![ini_cookies](https://user-images.githubusercontent.com/89120989/173222852-270b5268-79c2-4a42-a2e0-0abcace8b488.png)


---


## FLAG:
```
picoCTF{3v3ry1_l0v3s_c00k135_94190c8a}
```

