# Magikarp Ground Mission
#### Write-up author: [jon-brandy]()
## DESCRIPTION:
Do you know how to move between directories and read files in the shell? 
Start the container, `ssh` to it, and then `ls` once connected to begin. 
Login via `ssh` as `ctf-player` with the password, `6dee9772`.
## HINT:
1. Finding a cheatsheet for bash would be really helpful!
## STEPS:
1. First, launch the machine.
2. Next, enter the `ssh` given by pico -> `ssh ctf-player@venus.picoctf.net -p 53408`.
3. After that, enter the password as -> `6dee9772`.

> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/181175862-bbcff69b-78b0-485f-af58-08f83e6e4be0.png)

4. Then i run `ls`, to see every file available.

> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/181176059-950a34b3-118e-420d-8347-5bd5127c5be7.png)

5. Now, let's see what inside both `.txt` file by run `cat` command.

> OUTPUT OF 1of3.flag.txt

![image](https://user-images.githubusercontent.com/70703371/181176287-1070cdc6-1c89-448e-a5e6-d2f722ec2a15.png)

```
picoCTF{xxsh_
```

> OUTPUT OF instructions-to-2of3.txt

![image](https://user-images.githubusercontent.com/70703371/181176387-0c697874-a951-44ca-a948-739a6afa7719.png)

```
Next, go to the root of all things, more succinctly `/`
```

6. Let's run `cd` then to go out from the current folder we are in, then run `ls` again to see every files we have.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/181176655-d5ce73d2-a9ac-4962-bfaf-e633dddeb8ea.png)

7. Run `cat` again to `3of3.flag.txt`.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/181176830-96c53564-1cdb-4bac-b3eb-68f54f15972d.png)

```
540e4e79}
```

8. We got the first piece and the last piece, but lack of the 2nd piece.
9. I run `cd ..` to go back one folder (bsed from the instructions-to-2of3.txt) , then run `ls` again.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/181177893-8773da1f-da0e-496f-8cf8-83b5310f43e5.png)

10. I run the same thing -> `cd ..`.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/181178174-a5bbf2bb-1bec-47f8-aca6-51ec8b13760e.png)

11. We found it!

> OUTPUT OF 2of3.flag.txt

```
0ut_0f_\/\/4t3r_
```

12. Concate every piece of the flag.

> RESULT

```
picoCTF{xxsh_0ut_0f_\/\/4t3r_540e4e79}
```

12. Finally we got the flag!

---

## FLAG

```
picoCTF{xxsh_0ut_0f_\/\/4t3r_540e4e79}
```

