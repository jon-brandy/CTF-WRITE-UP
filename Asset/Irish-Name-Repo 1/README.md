# Irish-Name-Repo 1
### Write-Up Author : jon-brandy
## DESCRIPTION:
There is a website running at https://jupiter.challenges.picoctf.org/problem/50009/ [(link)](https://jupiter.challenges.picoctf.org/problem/50009/) 
or http://jupiter.challenges.picoctf.org:50009. Do you think you can log us in? Try to see if you can login!
## HINTS:
1. There doesn't seem to be many ways to interact with this. I wonder if the users are kept in a database?
2. Try to think about how the website verifies your login.
## STEPS:
1. Based from the hint number one, we can conclude that we may use `SQLi`.
2. Try to open the `admin login` tab.

![Screenshot (436)](https://user-images.githubusercontent.com/70703371/173019650-80205ce8-6b0a-4dc1-a70e-19fb3c60d7e1.png)

3. Next, on the username textarea, insert this command `admin'--` and leave the password textarea to blank.

![Screenshot (437)](https://user-images.githubusercontent.com/70703371/173019917-8ad75669-0e4c-42c6-9c04-3b8eded1511c.png)

4. Last, click the `login` button.

![Screenshot (438)](https://user-images.githubusercontent.com/70703371/173020187-7813f5b5-f349-4b6d-ae84-7b76b48e9575.png)

5. Finally we got the flag!


---

## FLAG:
```
picoCTF{s0m3_SQL_fb3fe2ad}
```
