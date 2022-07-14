# Matryoshka doll
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. 
What's the final one? Image: [this]()
## HINTS:
1. Wait, you can hide files inside files? But how do you find them?
2. Make sure to submit the flag as picoCTF{XXXXX}
## STEPS:
1. First, download the file given.
2. Based from the hint number 1, to check file hidden inside a file, simply run `binwalk`.

```
binwalk dolls.jpg
```
![image](https://user-images.githubusercontent.com/70703371/178897990-975d58f3-f50b-460c-aa06-d60ec5b309d0.png)

3. Seems we found a hidden file there. To extract it run this command:

```
foremost dolls.jpg
```

4. Now open the  `output` folder.

![image](https://user-images.githubusercontent.com/70703371/178898126-5bfa9558-0f70-4522-8399-5d9c6aa9d8d0.png)

![image](https://user-images.githubusercontent.com/70703371/178898177-26cc3238-c450-4824-98c0-68e96b477359.png)

5. Open the `zip` folder and run ls to see what's inside!

![image](https://user-images.githubusercontent.com/70703371/178898290-d6e759fd-40b5-459b-b912-61e59527c06a.png)

6. Let's unzip it by run this command:

```
unzip 00000532.zip
```
7. We got another file!

![image](https://user-images.githubusercontent.com/70703371/178898426-16091917-edfa-432f-a263-7942f584e46d.png)

8. Open the `base_images` folder and run `ls` to see what's inside.

![image](https://user-images.githubusercontent.com/70703371/178898855-299a3331-4de3-4de8-8517-0bae2a6c16fa.png)

9. Run `binwalk` again to see are there still hidden files insde.

![image](https://user-images.githubusercontent.com/70703371/178899036-43628c15-de14-4ad8-ba9c-63578aaa1712.png)

10. There is.
11. Now run foremost again
12. Open the `output` folder -> `zip` , unzip the zipped file.

![image](https://user-images.githubusercontent.com/70703371/178899277-3c77302c-4548-4b9a-bc4a-470fbff37386.png)

![image](https://user-images.githubusercontent.com/70703371/178899449-fe3b3e1c-8cf3-4eb3-8c49-a45f8c088392.png)

13. Open the `base_images` folder, then run binwalk again.

![image](https://user-images.githubusercontent.com/70703371/178899502-88110655-588d-43d8-b5ed-ffeb6d953cc4.png)

14. Do the same step as before!
15. Looks like this time is the flag file.

![image](https://user-images.githubusercontent.com/70703371/178899682-40a9fc2d-1bdd-43df-bc7e-5f3d0877bae3.png)

![image](https://user-images.githubusercontent.com/70703371/178899800-2c4607fe-f2f3-474f-81b8-cff3d90e49c7.png)

![image](https://user-images.githubusercontent.com/70703371/178899834-ed5397c0-ca2b-4ccc-970a-03d69037d583.png)

16. Finally, we got the flag!

![image](https://user-images.githubusercontent.com/70703371/178899924-fb903969-ef12-4c08-b6f6-df78b1b2901e.png)


---
## FLAG:

```
picoCTF{bf6acf878dcbd752f4721e41b1b1b66b}
```

## REFERENCES:
```
https://www.kali.org/tools/binwalk/
```



