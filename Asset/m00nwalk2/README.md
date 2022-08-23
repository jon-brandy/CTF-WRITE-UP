# m00nwalk2
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Revisit the last [transmission](https://github.com/jon-brandy/CTF-WRITE-UP/blob/d7461443403a3cf9feb925e15a85feeeccb40d5e/Asset/m00nwalk2/message.wav). 
We think this transmission contains a hidden message. There are also some clues [clue 1](https://github.com/jon-brandy/CTF-WRITE-UP/blob/d7461443403a3cf9feb925e15a85feeeccb40d5e/Asset/m00nwalk2/clue1.wav), [clue 2](https://github.com/jon-brandy/CTF-WRITE-UP/blob/d7461443403a3cf9feb925e15a85feeeccb40d5e/Asset/m00nwalk2/clue2.wav), [clue 3](https://github.com/jon-brandy/CTF-WRITE-UP/blob/d7461443403a3cf9feb925e15a85feeeccb40d5e/Asset/m00nwalk2/clue3.wav).
## HINT:
1. Use the clues to extract the another flag from the .wav file.
## STEPS:
1. First, download all the files given.
2. I think we may use the same step as the `m00nwalk` challenge.
3. So i open `RXSSTV` and play the audio at my phone (set the phone as the speaker) and select `scottie 1` as the mode.

> MESSAGE.WAV

![image](https://user-images.githubusercontent.com/70703371/186167745-e66c12de-07a5-4987-978f-519c98a9ce34.png)

> CLUE1.WAV -> i use Martin 1 as the mode.

![image](https://user-images.githubusercontent.com/70703371/186168966-b02552c3-be23-4169-8482-bc7459bcf818.png)

> CLUE2.WAV -> i use scottie 2 as the mode.

![image](https://user-images.githubusercontent.com/70703371/186170230-425f5143-89be-41cd-8016-5cc3b7ac143a.png)

> CLUE3.WAV

![image](https://user-images.githubusercontent.com/70703371/186170721-a334440f-0d01-4180-9aca-5f184f06b222.png)

4. Hmm.. From all of the images we received, seems there's two images that caught my attention.
5. The first one is the `stego` , it's obvious we may use tools related to **steganography** and the password for extraction is `hidden_password`. For the `future boys` image, if we try to search that on the internet.
6. I found this.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/186171559-3a6fc0b9-f21f-44e9-bb65-abce9dc3e4fd.png)

7. Now it's more obvious that it's a steganography.
8. For this solution i used `steghide`.
9. Run this command -> `steghide extract -sf message.wav -p hidden_stegosaurus`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/186172610-c71a219d-51ff-4b15-8bdf-b640ba894574.png)

10. Open the extracted `.txt` file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/186172835-89330947-b5bc-4b41-9d21-ce3b17af38bb.png)


11. Finally, we got the flag!

## FLAG

```
picoCTF{the_answer_lies_hidden_in_plain_sight}
```
