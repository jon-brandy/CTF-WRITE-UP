# SOAP
> Write-up author: jon-brandy
## DESCRIPTION:
The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?

Additional details will be available after launching your challenge instance.
## HINT:
- NONE
## STEPS:
1. In this challenge we're given a web app which vuln with XXE (by the tag).
2. Let's use burpsuite to exploit the request body it sent to the server.

> Click the details button so we can capture the request in burp.

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/c2914963-e6a6-4b1d-abb6-7e0f2ef6383b)


![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/2360b8e2-e22d-42ae-a407-f4bb40742ec5)


3. Based from the description, we know the goals is to read `/etc/passwd` file.
4. I used this template payload from --> `https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XXE%20Injection`.

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/7c755e76-d4ea-402c-a6a0-7315fd6409a0)


```xml
<?xml version="1.0"?><!DOCTYPE root [<!ENTITY xxe SYSTEM 'file:///etc/passwd'>]>
<data><ID>&xxe;</ID></data>
```

> RESULT

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/aac2cc06-f351-4670-907b-a1bde8e66052)


5. Got the flag!

## FLAG

```
picoCTF{XML_3xtern@l_3nt1t1ty_0e13660d}
```
