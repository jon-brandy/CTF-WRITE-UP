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

