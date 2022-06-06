# GET aHEAD
## DESCRIPTION:
- Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:45028/

## HINTS:
1. Maybe you have more than 2 choices.
2. Check out tools like Burpsuite to modify your requests and look at the responses

## STEPS:

1. First, open the following website `http://mercury.picoctf.net:45028/`

![Screenshot (379)](https://user-images.githubusercontent.com/98648342/170867694-f055b689-af7f-412b-89b2-81eeca34cf60.png)

2. Next, open burpsuite and set the `intercept to on` and we refresh the website.

![Screenshot (384)](https://user-images.githubusercontent.com/98648342/170867754-a8556bb9-fecd-42b4-89ce-e43d592d9378.png)

3. Then, click the `action` button, and choose `send to repeater`.

![Screenshot (385)](https://user-images.githubusercontent.com/98648342/170867902-c14bb974-7dfb-40da-a511-300dafbfc200.png)

4. Click the `send` button.

![Screenshot (386)](https://user-images.githubusercontent.com/98648342/170867919-ab18e8a6-416c-4a78-a5da-6bd4733c84e6.png)

5. Finally we can see the source code. With repeater we can manually manipulating and reissuing individual HTTP requests, and analyzing the application's responses.

![Screenshot (387)](https://user-images.githubusercontent.com/98648342/170867983-c468bf5a-16e3-4c75-8e5d-9057e8cdde7b.png)

6. From the source code we can see there's two method, `POST` and `GET`.

![Screenshot (388)](https://user-images.githubusercontent.com/98648342/170868047-719ad1e0-0b8a-478c-b929-f9c385cab40e.png)

7. We can try to change the method from GET to HEAD.

![Screenshot (389)](https://user-images.githubusercontent.com/98648342/170868093-0211a3d8-9c05-4e65-b2a7-2052e3265b5d.png)

8. After changing that, click again the `send` button, and finally we can see the flag!

![Screenshot (390)](https://user-images.githubusercontent.com/98648342/170868113-e1759627-4235-445e-bd86-7ec21b5e53df.png)


---

## FLAG:
```
picoCTF{r3j3ct_th3_du4l1ty_775f2530}
```
