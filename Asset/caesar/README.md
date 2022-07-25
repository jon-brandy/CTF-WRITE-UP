# caesar
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Decrypt this [message]().
## HINT:
1. caesar cipher [tutorial](https://privacycanada.net/classical-encryption/caesar-cipher/).
## STEPS:
1. First, download the file given.
2. Based from the hint and the description, we can guess that it might be a caesar cipher text.
3. Now, let's see what's inside this file by run -> `strings ciphertext`.

![image](https://user-images.githubusercontent.com/70703371/180725030-f5e1a640-bb4e-4312-b077-0daa4242f902.png)

4. Looks like we just have to decode the text inside the curly brackets.
5. For this solution i used [this](https://cryptii.com/pipes/caesar-cipher) online decoder.
6. Paste the ciphertext and change the shifted value until the plaintext become a coherent message.

![image](https://user-images.githubusercontent.com/70703371/180726612-06f8a7c7-d183-4fde-8b24-c7096e3f5c6a.png)

7. Finally we got the flag!

```
picoCTF{crossingtherubiconvfhsjkou}
```
