# logon
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
The factory is hiding things from all of its users. 
Can you login as Joe and find what they've been looking at? 
https://jupiter.challenges.picoctf.org/problem/15796/ [(link)](https://jupiter.challenges.picoctf.org/problem/15796/) or http://jupiter.challenges.picoctf.org:15796
## HINT:
1. Hmm it doesn't seem to check anyone's password, except for Joe's?
## STEPS:
1. Try to insert the username as `admin` and leave the password form to blank.
2. The website will tells us this.

![Screenshot (427)](https://user-images.githubusercontent.com/70703371/172981076-e4ca65de-cf9f-4df5-81e1-55ba590cf63c.png)

3. But if we insert the username as **Joe**. The website will give us this response:

![Screenshot (428)](https://user-images.githubusercontent.com/70703371/172981375-a79aa038-e7be-421f-84c3-c62b4d11d56c.png)

4. Now, open `inspect element` and check the cookies at the `storage` tab.

![Screenshot (432)](https://user-images.githubusercontent.com/70703371/172981922-3fd78e05-2232-4cc1-a26d-7736c29d19f2.png)

5. Change the `admin` value to `True` and refresh the page.
6. Finally, we got the flag!

![Screenshot (433)](https://user-images.githubusercontent.com/70703371/172982013-03baafb1-ba29-457d-b730-28523c954b7a.png)

---


## FLAG:
```
picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}
```
