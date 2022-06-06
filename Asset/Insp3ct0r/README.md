# Insp3ct0r
## DESCRIPTION:
Kishor Balan tipped us off that the following code 
may need inspection: ```https://jupiter.challenges.picoctf.org/problem/44924/``` or http://jupiter.challenges.picoctf.org:44924
## HINTS:
1. How do you inspect web code on a browser?
2. There's 3 parts
## STEPS:
1. Based from the hint, try to inspect the source code of the website.
2. We can see that there are 3 files.

![Screenshot (110)](https://user-images.githubusercontent.com/98648342/172037482-d74f0075-d14a-4cab-927c-cc554ef09bc5.png)

3. Try to check the HTML file first. At the line number 31, we get the first part of the flag.

![Screenshot (111)](https://user-images.githubusercontent.com/98648342/172037533-625639e4-a5d8-42dc-9e3c-64c76fe20b71.png)

4. Next, try to inspect the CSS file. At the line number 51, we can see the comment give us the second part of the flag.

![Screenshot (112)](https://user-images.githubusercontent.com/98648342/172037599-c4552212-521a-4915-b8ca-628ba6e4c893.png)

5. Then, try to check the last source code file, the JS. At the line number 21, there is the last part of the flag.

![Screenshot (113)](https://user-images.githubusercontent.com/98648342/172037624-a37d3b41-24e6-4344-9500-adeb6db8d97c.png)

6. Finally we just have to concate all of the 3 parts we got.

---

## FLAG:
```
picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?f10be399}
```
