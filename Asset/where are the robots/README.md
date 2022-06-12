# where are the robots
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Can you find the robots? ```https://jupiter.challenges.picoctf.org/problem/60915/``` or http://jupiter.challenges.picoctf.org:60915
## HINTS:
What part of the website could tell you where the creator doesn't want you to look?
## STEPS:
1. We can try to check hidden file(s) inside the website using tools that are similiar to `dirbuster` and `gobuster`. It is called `DIRB`.
2. Try to run the command `dirb https://jupiter.challenges.picoctf.org/problem/60915/ -X .txt`. `-X` means extension, so basically from the command means we want to check are there any file(s) hidden in this website that has the `.txt` extension.
3. Then click enter.
4. This might be took a few minutes.
5. Finally we got this output:

![Screenshot (114)](https://user-images.githubusercontent.com/98648342/172039721-3b7f20fd-2f71-4b10-b2a2-9b5675373318.png)

6. From the output we got information, that there is a `robots.txt` file inside the website.
7. Try to change the url to `https://jupiter.challenges.picoctf.org/problem/60915/robots.txt`.
8. Then the page changed to this:

![Screenshot (115)](https://user-images.githubusercontent.com/98648342/172039910-e685b71e-8e16-474e-8f0f-d0ed72e3cc0d.png)

9. The last step, try to change the url using the Disallow mentioned. `/8028f.html` -> `https://jupiter.challenges.picoctf.org/problem/60915/8028f.html`
10. Finally, we can see the flag.

![Screenshot (116)](https://user-images.githubusercontent.com/98648342/172039979-46c21bc8-d67c-40c4-b407-c39988f7e817.png)

---
## FLAG:
```
picoCTF{ca1cu1at1ng_Mach1n3s_8028f}
```
