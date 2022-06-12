# Power Cookie
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Can you get the flag? Go to this [website](http://saturn.picoctf.net:61304/) and see what you can discover.
## HINT:
1. Do you know how to modify cookies?
## STEPS:
1. Try to click the `Continue as guest` button.
2. Next, the website tells us this.

![Screenshot (414)](https://user-images.githubusercontent.com/70703371/172818564-577efbf8-a71f-43f9-bd5e-02e3ecef94b1.png)

3. Then, based from the hint, try to open the `inspect element`.
4. Go to `storage` tab.
5. We can see that there's a cookie says:

![Screenshot (415)](https://user-images.githubusercontent.com/70703371/172818941-56988f2f-2da1-43c4-8f80-b8a09dcdc1fd.png)

6. Now try to change the `isAdmin` value to 1.
7. Last, try to refresh the page.
8. Finally we get the flag!

![Screenshot (416)](https://user-images.githubusercontent.com/70703371/172819262-7b2e0b2a-ef2d-4d6e-9026-6abf7aa095d0.png)


---

```
picoCTF{gr4d3_A_c00k13_0d351e23}
```



