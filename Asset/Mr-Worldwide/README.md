# Mr-Worldwide
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
A musician left us a [message](https://github.com/jon-brandy/CTF-WRITE-UP/blob/4032f8dc04676c96fd383d537c383b4132f8c9cf/Asset/Mr-Worldwide/message.txt). What's it mean?
## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Since it's a `.txt` file, let's see what strings inside by run -> `strings message.txt`.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/180767415-04347041-e709-4311-b62c-0c973759fc3a.png)

3. At first, i didn't get what it means. But there's something that caught my attention.
4. The one with minus value.

![image](https://user-images.githubusercontent.com/70703371/180767596-43297ce8-8524-408f-a8b2-69abec9d4a85.png)

5. It reminds me of an `(x, y)` coordinate?
6. So i opened google maps, and paste the coordianates at the `search` area and got this!

![image](https://user-images.githubusercontent.com/70703371/180768033-9a934143-cab4-4ed1-bc23-5faa79e4b62d.png)

7. Hmm Dayton.. Might be just a coincidence, so i tried another value, this time i tried the first one.

![image](https://user-images.githubusercontent.com/70703371/180768244-e549c13a-845a-45cb-b1d8-72a13d238c83.png)

8. This time Kyoto. I think it really does a coordinates, so i tried to concate every each one of them from the start.

> OUTPUT:

```
Kyoto, Odessa, Dayton, Istanbul, Abu Dhabi, Kuala Lumpur, _ Adis Ababa, Loja, Amsterdam, Sleepy Hollow, Kodiak, Alexandria Governorate
```

9. It does confusing, either i took the region or the city name of it. I tried to took every each and took the first character of each string and concate them. But the one which the `web` accept is flag from the name above.
10. If i took every first index of the string, it will give us:

```
KODIAK_ALASKA
```

11. Finally just wrap it around with `picoCTF{}`.

---

## FLAG

```
picoCTF{KODIAK_ALASKA}
```

**NOTES**:

```
I think there's an intended solution for this challenge.
```


