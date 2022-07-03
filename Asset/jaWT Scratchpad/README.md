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
8. At your kali linux, paste the token into any file name with `.john` extension. For example i named the file `jwt.john`.
9. For the wordlist i used `rockyou.txt` which you can download [here](https://drive.google.com/file/d/1oKHoc6s03-hi40vlBzkPywUR4_NPAPhX/view?usp=sharing).

> REASONS TO USE rockyou.txt AND NOT password.lst (on the john folder), because it is known as the best password dictionary.

```
BEST PASSWORD DICTIONARY : https://cryptokait.com/2020/09/02/taking-password-cracking-to-the-next-level/
```

10. Now on your kali linux terminal type this command:

```sh
john --wordlist=/home/[your_username]/Downloads/rockyou.txt --rules jwt.john 
```

![image](https://user-images.githubusercontent.com/70703371/177024153-6d13a21a-1a23-46dc-a3c9-f23c664f9f66.png)

11. Next using [this](https://jwt.io/) online tools , at the `decode` tab, change the user value to `admin`. Also change the jwtsign at the `Verify Signature` section to `ilovepico`.

![image](https://user-images.githubusercontent.com/70703371/177024606-6009963e-b6c6-435c-9b15-4912b70419b6.png)


![image](https://user-images.githubusercontent.com/70703371/177024758-b310e3e3-e6ce-4a6f-be7e-397c114523ae.png)


12. Now the signature does verified!

![image](https://user-images.githubusercontent.com/70703371/177024804-a16f1f43-8c47-43de-9ef2-47d81e299c4a.png)

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.gtqDl4jVDvNbEe_JYEZTN19Vx6X9NNZtRVbKPBkhO-s
```

13. Now open the the challenge's website again, then register as any name you want then change the jwt token value to -> eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.gtqDl4jVDvNbEe_JYEZTN19Vx6X9NNZtRVbKPBkhO-s

14. Refresh it!

![image](https://user-images.githubusercontent.com/70703371/177024851-8395e24b-5ec9-449b-90b8-57694c418bd4.png)

15. Finally we got the flag!


---
## FLAG:
```
picoCTF{jawt_was_just_what_you_thought_44c752f5}
```


## REFERENCES:
```
https://cryptokait.com/2020/09/02/taking-password-cracking-to-the-next-level/
https://wiki.skullsecurity.org/index.php/Passwords#Password_dictionaries
https://askubuntu.com/questions/866596/you-do-not-have-permission-to-extract-to-this-folder
https://jwt.io/introduction
```
