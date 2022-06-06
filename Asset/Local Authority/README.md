# Local Authority
## DESCRIPTION:
Can you get the flag?
Go to this [website](http://saturn.picoctf.net:55826) and see what you can discover.
## HINTS:
1. How is the password checked on this website?
## STEPS:
1. Try to insert the username `admin` and the password also `admin`.
2. We can see that the login page says `Log In Failed`. But try to inspect the element.

![Screenshot (399)](https://user-images.githubusercontent.com/98648342/172052063-4b2176ad-9834-4972-b3ae-a3f44276527b.png)

3. Try to open the `secure.js` file. From that file, we can see a function like this.

![Screenshot (399)](https://user-images.githubusercontent.com/98648342/172052118-8c587eee-2fd6-4ca2-b1a9-d906fecfc913.png)

4. Now let's try to insert the username as `admin` and the password as `strongPassword098765`
5. Finally we can see the flag!

![Screenshot (400)](https://user-images.githubusercontent.com/98648342/172052269-fbce4e2c-418d-4e91-80fb-6033f4afbbf0.png)

---

## FLAG:
```
picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}
```
