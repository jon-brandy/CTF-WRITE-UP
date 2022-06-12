# rail-fence
#### Write-up author : [Q](https://github.com/tkxldk)
## DESCRIPTION:
A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). 
Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it?
Download the message [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/90fd5fed520ba9f7b28f2b998f1a4e831058bc3a/Asset/rail-fence/message%20(1).txt).
Put the decoded message in the picoCTF flag format, `picoCTF{decoded_message}`.
## HINT:
Once you've understood how the cipher works, it's best to draw it out yourself on paper

## STEPS:
1. Download the file
2. Open a Rail Fence Cipher Decryptor, i use this [web](https://www.boxentriq.com/code-breaking/rail-fence-cipher)
3. Then set the rails to 4 and the offset to 0

![image](https://user-images.githubusercontent.com/89120989/173226151-1ad4f3f7-1333-4f15-9696-437028a31107.png)

4. Wala, you get the flag!

---


## FLAG:
```
picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_4A76B997}
```
