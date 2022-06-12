# Information
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## Hints:
1. Look at the details of the file
2. Make sure to submit the flag as picoCTF{XXXXX}

## Steps:
1. First download the `cat.jpg` file from the challenge.
2. Second, try to check the file type first, by run command `file cat.jpg`.

![Screenshot (340)](https://user-images.githubusercontent.com/98648342/169524689-57d7cdd9-4aab-431f-be51-a231f9c5c7e2.png)

3. From the output, we know that the image type is JPEG, so change to JPEG first by run this command `mv cat.jpg cat.jpeg`.

![Screenshot (341)](https://user-images.githubusercontent.com/98648342/169524836-132d35a4-ed14-41cb-965b-bbe5477c5652.png)

4. Now we can try `strings cat.jpeg`.
5. From here we can see there's so many strings and it is almost impossible to see the flag. So we shall try `strings cat.jpeg | grep picoCTF{`.

![Screenshot (344)](https://user-images.githubusercontent.com/98648342/169525924-84ebbd61-fa28-4cd4-8adf-d01e2ffc44bf.png)

6. But we don't get any output.
7. So maybe we can use `hexedit`.
8. But when i try `strings cat.jpg` and i scroll up, i found this.

![Screenshot (343)](https://user-images.githubusercontent.com/98648342/169526342-24e1ac3d-658d-4af1-a398-a11680cd6968.png)

9. It looks like some kind of base64.
10. So just try both of them -> `W5M0MpCehiHzreSzNTczkc9d` , `cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9`
11. We can try this command -> `echo W5M0MpCehiHzreSzNTczkc9d | base64 -d`. Reminder `-d` means decode.

![Screenshot (345)](https://user-images.githubusercontent.com/98648342/169527615-261caa7c-7124-417f-a511-43dd2f59bf43.png)

12. After executed the command, we got undefined strings. So let's try the other base64 text!

![Screenshot (346)](https://user-images.githubusercontent.com/98648342/169528056-ab31ba4e-9666-452e-bbf1-e25d17e56856.png)

13. Finally we got the flag!


---

## FLAG
```
picoCTF{the_m3tadata_1s_modified}
```
