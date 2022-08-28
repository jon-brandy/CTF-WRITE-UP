# X marks the spot
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Another login you have to bypass. Maybe you can find an injection that works? `http://mercury.picoctf.net:20297/`.
## HINT:
1. XPATH.
## STEPS:
1. First, open the link given.

![image](https://user-images.githubusercontent.com/70703371/187067536-38ad8178-21a1-4e41-8cfe-92e1d97d15af.png)

2. Based from the hint, i think this is a XPATH injection (?)

> NOTES ABOUT XPATH

```
https://owasp.org/www-community/attacks/XPATH_Injection
```

3. Since this is the first the first time i heard about it, so it took a while for me to solve this challenge.
4. First i tried to input -> `' or 1=1 or 'admin`, which means it always true and i put it in the **username** textarea.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/187067833-20b3100f-cd67-49d7-9f2c-3bc8720eeb14.png)

5. Well our query succeeded, but we did not get redirected to some sort of application. Which means it is a **BLIND XPATH INJECTION**.



## FLAG

```
```


## REFERENCES:

```
https://owasp.org/www-community/attacks/XPATH_Injection
https://book.hacktricks.xyz/pentesting-web/xpath-injection
```
