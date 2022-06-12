# picobrowser
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
This website can be rendered only by **picobrowser**, go and catch the flag! 
https://jupiter.challenges.picoctf.org/problem/50522/ [(link)](https://jupiter.challenges.picoctf.org/problem/50522/) or http://jupiter.challenges.picoctf.org:50522
## HINT:
1. You don't need to download a new web browser
## STEPS:
1. Click the link given.
2. Try to click the `flag` button and see what's happen.
3. Seems the website tells us that we must use the **picobrowser**.

![Screenshot (423)](https://user-images.githubusercontent.com/70703371/172979400-609e33ed-99df-4a98-a615-e2ae50434bda.png)

4. Now, open BurpSuite and set the `intercept` to on.
5. Next, try to refresh the page so we can capture request.
6. Then, click the `action` button and choose `send to repeater`.

![Screenshot (424)](https://user-images.githubusercontent.com/70703371/172979972-93a49b20-3242-4d6d-81f4-4d1aa2b17b7a.png)

7. Open the `repeater` tab and click the `send` button.

![Screenshot (425)](https://user-images.githubusercontent.com/70703371/172980034-56bf5c0c-2593-4cf9-a406-4d1459e588c1.png)

8. Change the `User-Agent` value to -> **picobrowser**. Click the `send` button again.
9. Finally, we can see the flag on the `response` page.

![Screenshot (426)](https://user-images.githubusercontent.com/70703371/172980235-7d2c301d-a66b-46a9-865b-ef6a55fd3004.png)


---

## FLAG:
```
picoCTF{p1c0_s3cr3t_ag3nt_51414fa7}
```
