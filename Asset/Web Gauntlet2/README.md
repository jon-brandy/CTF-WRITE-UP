# Web Gauntlet 2
## DESCRIPTION:
```
If the flag is not displayed after completing this challenge, try clearing your cookies. 
Cookies set by other challenges may prevent the flag from displaying properly.
```
This website looks familiar... 
Log in as admin Site: http://mercury.picoctf.net:57359/ Filter: http://mercury.picoctf.net:57359/filter.php
## HINTS:
1. I tried to make it a little bit less contrived since the mini competition.
2. Each filter is separated by a space. Spaces are not filtered.
3. There is only 1 round this time, when you beat it the flag will be in filter.php.
4. There is a length component now.
5. sqlite
## STEPS:
1. First, open the website -> `http://mercury.picoctf.net:57359/`.
2. Try to input the user as `admin` and password as `admin`, then click `sign in`.

![image](https://user-images.githubusercontent.com/70703371/176359524-bab1d32f-97e3-4980-877b-5a5bded8da4e.png)

3. It said `filtered`.

![image](https://user-images.githubusercontent.com/70703371/176359641-89709f85-be71-4337-92db-4076df442cf4.png)

4. Now try to open the `http://mercury.picoctf.net:57359/filter.php`.

![image](https://user-images.githubusercontent.com/70703371/176359789-e76bcf1f-3ae7-4b37-9442-4a0a219dfc61.png)

5. We can conclude that the website does filter few entities.
6. Next, let's try to input the unfiltered word, in this case i tried to input `user` as username and `pass` as password.

![image](https://user-images.githubusercontent.com/70703371/176362401-8ebc806b-c876-4a01-9b8b-4461cef2d38f.png)

7. It said `not admin`. Means we must use the username as `admin` but we need to bypass it.

![image](https://user-images.githubusercontent.com/70703371/176362494-61d82bab-62a9-427c-9241-39ac94184a14.png)

8. The easiest bypass is to use `||` for concatenation. Now input `adm'||'in` as username.
9. For the password  




