# Super Serial
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Try to recover the flag stored on this website http://mercury.picoctf.net:25395/
## HINT:
The flag is at ../flag
## STEPS:
1. First, open the website given.
2. For this solution i used `gobuster` to check hidden directory from this website.
3. Run this command:

```bash
gobuster dir -e -u http://mercury.picoctf.net:25395/ -w /usr/share/wordlists/dirb/common.txt
```
> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/179447007-accc6d10-6c10-4ffe-8971-5537fa6a3893.png)

![image](https://user-images.githubusercontent.com/70703371/179447083-0970fc86-afc8-4940-bd37-375570ca7cfa.png)

4. Now let's open `robots.txt` by change the url to this `http://mercury.picoctf.net:25395/robots.txt`.

> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/179447163-dbb17cf7-003e-4e1d-8a79-fc10c352af66.png)

5. Now go to the `admin.phps` by change the url to this -> `http://mercury.picoctf.net:25395/robots.txt/admin.phps/`

> OUTPUT:
