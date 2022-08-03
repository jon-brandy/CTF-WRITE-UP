# SideChannel
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag? 
Download the PIN checker program here [pin_checker](). Once you've figured out the PIN (and gotten the checker program to accept it), 
connect to the master server using nc saturn.picoctf.net 52680 and provide it the PIN to get your flag.
## HINTS:
1. Read about "timing-based side-channel attacks."
2. Attempting to reverse-engineer or exploit the binary won't help you, you can figure out the PIN just by interacting with it and measuring certain properties about it.
3. Don't run your attacks against the master server, it is secured against them. The PIN code you get from the `pin_checker` binary is the same as the one for the master server.
## STEPS:
1. First, download the PIN checker program.
2. Check the file type.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182294601-2f86d474-a736-4790-8e0b-fb6c9c1eb75f.png)

3. Let's make it executable by run -> `chmod +x pin_checker`.
4. Now run it by -> `./pin_checker`.

![image](https://user-images.githubusercontent.com/70703371/182294796-ab384ba3-f2c8-4764-8f30-12bf0640c378.png)

5. Based from the hint number 1, let's do small research about `timing based side-channel attacks`.

> NOTES

```
In cryptography, a timing attack is a side-channel attack in which the attacker attempts to compromise a cryptosystem by analyzing the time taken to execute cryptographic algorithms. 

Every logical operation in a computer takes time to execute, and the time can differ based on the input; with precise measurements of the time for each operation, an attacker can work backwards to the input. 

Finding secrets through timing information may be significantly easier than using cryptanalysis of known plaintext, ciphertext pairs. Sometimes timing information is combined with cryptanalysis to increase the rate of information leakage.
```

6. Since i can't make the `python` script, so i bruteforced it.
7. At first, i started by enter `00000000`.
8. Run the program again at your kali linux using this command -> `time ./pin_checker`.

> NOTES:

```
The "time" command -> In computing, time is a command in Unix and Unix-like operating systems. It is used to determine the duration of execution of a particular command.
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182574263-4ea212f5-6e34-44d4-9eba-84f1d86cb914.png)

9. Next, let's input `10000000`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182574853-1d5cfc69-e8aa-4ec6-bc97-400df0e40f7b.png)

10. it shows the same time, now let's try `20000000`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182574927-0c814f49-adad-4e30-8428-5724f2a38603.png)

11. Hmm.. Still the same, let's try `30000000`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182574975-848d1a2c-42a0-4697-83d5-d8e8e29a90ef.png)

12. Well, this time higher. Let's continue by `40000000`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182575107-9474d811-1370-4ae4-8a8d-f9966b1435b3.png)

13. Great! It's much higher, continue by `50000000`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182575321-f1d54160-0536-4d2b-a7d0-5f5e28bf4e99.png)

14. I keep doing this until `90000000`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182575447-8dc176e1-ba3f-4361-b159-141b6c302fae.png)

25. It's known that `40000000` is the highest time value.
26. I keep the value by incrementing to `41000000`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182575683-84f5d4c0-11ad-4bdd-933a-9e59ec3c4580.png)

27. Until `9`.
28. It's known that `48000000` has the highest time value.

![image](https://user-images.githubusercontent.com/70703371/182576071-0cebb53c-0b90-4ae3-91f0-41d26a745b9e.png)

29. Let's use the same steps until the last integer.

> FINAL RESULT

30. For the last digit, when i incremented it to -> `3`. The program gave me this output.

![image](https://user-images.githubusercontent.com/70703371/182577003-3fe7b1fa-2f76-4e8f-98d5-14dc69bc920b.png)

31. We can conclude that `48390513` is the right pin.
32. Now, run the netcat command -> `nc saturn.picoctf.net 52680` and enter the pin.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182577414-1f391da6-e2b6-4c12-8d0e-ac1e94952534.png)

33. Finally, we got the flag!

---

## FLAG

```
picoCTF{t1m1ng_4tt4ck_914c5ec3}
```


## REFERENCES

```
https://en.wikipedia.org/wiki/Time_(Unix)
https://en.wikipedia.org/wiki/Timing_attack
```
