# Who are you?
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn 
http://mercury.picoctf.net:34588/
## HINT:
1. It ain't much, but it's an RFC https://tools.ietf.org/html/rfc2616
## STEPS:
1. First, open the link given.

![image](https://user-images.githubusercontent.com/70703371/182081010-82b3b6c2-355c-4310-84c7-588f05c1c680.png)

2. Seems we have to change the `user-agent` value.
3. For this solution i used `burpsuite`. So i paste the url using `burpsuite` browser.

> CHOOSE SEND TO REPEATER

![image](https://user-images.githubusercontent.com/70703371/182081571-109120dc-b5c2-438d-af16-00cf88ffa9cc.png)

> OPEN REPEATER TAB CLICK THE SEND BUTTON

![image](https://user-images.githubusercontent.com/70703371/182081623-6d47c5d2-3e70-436a-9769-187d65d1b82a.png)

4. Change the `user-agent` value to `PicoBrowser` then click the `send` button again.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182081891-1f304a8d-a0c5-4605-9584-329e5117a5ee.png)

5. The clue here is `from another site`, means we may have to add a header called `Referer` and input the url from the description as it's value, then press the `send` button.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182082840-c3d0f4c3-df58-418c-9a7c-56a05b1cf810.png)

6. Seems we are making new progress.
7. `Only worked in 2018` means we may have to add a new header again called `Date`.
8. Now add `Date: Mon, 1 Jan 2018 01:00:00 GMT` then press the `send` button.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182083191-ed04d5be-f8be-413d-b5b5-16c77b849c9a.png)

9. We're doing great so far.
10. `i don't trust users who can be tracked` means we must add `DNT` header and input the value as `1` (true).

> NOTES & RESEARCH LINK

```
Do Not Track (DNT) is a browser setting that sends a message to websites and advertising networks requesting that they don't track the user. Firefox, Internet Explorer and Safari provide DNT settings.

https://www.techtarget.com/whatis/definition/Do-Not-Track-DNT
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182083664-55ef45c6-4b71-434d-939c-85d86b2d5a5b.png)

12. `Is only for people from Sweden` means we have to change our IP.
13. Now add a header called `X-Forwarded-For` and input the value as `1.208.1.45`

> RESEARCH LINK

```
https://en.wikipedia.org/wiki/X-Forwarded-For
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For
```

14. 


## REFERENCES

```
http://www.lingoes.net/en/translator/langcode.htm
https://www.techtarget.com/whatis/definition/Do-Not-Track-DNT
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For
https://en.wikipedia.org/wiki/X-Forwarded-For
```
