# Easy1
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
The one time pad can be cryptographically secure, but not when you know the key. 
Can you solve this? We've given you the encrypted flag, key, and a table to help `UFJKXQZQUNB` with the key of `SOLVECRYPTO`. 
Can you use this table to solve it?. 
## HINTS:
1. Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.
2. Please use all caps for the message.
## STEPS:
1. First, download the file given.
2. Based from the description and the downloaded file. We can identify it's a vigenere cipher.

> FROM WIKIPEDIA

![image](https://user-images.githubusercontent.com/70703371/180722463-5894cf43-d039-438f-afa2-5e5984bd0c36.png)

3. For this solution, i used online [tools](https://www.boxentriq.com/code-breaking/vigenere-cipher)
4. Simply paste the **ciphertext** and the **key**, then press the `decode` button

![image](https://user-images.githubusercontent.com/70703371/180722732-97485cb6-5fec-41be-805b-5e18f8a18567.png)

> RESULT:

![image](https://user-images.githubusercontent.com/70703371/180722859-a57da278-e440-4198-b689-8f53778e714e.png)

5. Finally we just have to wrap the result with `picoCTF{}`

---

## FLAG

```
picoCTF{CRYPTOISFUN}
```

## REFERENCES

```
https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
```
