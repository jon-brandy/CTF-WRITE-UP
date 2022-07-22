# m00nwalk
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Decode this [message](https://github.com/jon-brandy/CTF-WRITE-UP/blob/f1c374c5e017a1a1e727f555d6fa81a7f4af7fc8/Asset/m00nwalk/message.wav) from the moon.
## HINTS:
1. How did pictures from the moon landing get sent back to Earth?
2. What is the CMU mascot?, that might help select a RX option
## STEPS:
1. First, download the file given.
2. Then, i tried to listen to the `.wav` file but didn't get any clue.
3. So i did small research at the clue number 1 and number 2.

> NOTES:
```
ANS FROM HINT NUMBER 1
----------------------
NASA selected a scan converter manufactured by RCA to convert the black-and-white SSTV signals from the Apollo 7, 8, 9 and 11 missions. When the Apollo TV camera radioed its images, the ground stations received its raw unconverted SSTV signal and split it into two branches.
```

```
ANS FROM HINT NUMBER 2
----------------------
Scotty the Scottie Dog
```

4. For this solution i used RXSSTV.

![image](https://user-images.githubusercontent.com/70703371/180455032-6a1775f8-ebe2-441a-b6cb-500b6894f133.png)

5. Play the audio at my phone and put it beside the mic, then press the following button at the `RXSSTV` software.

![image](https://user-images.githubusercontent.com/70703371/180455709-c87ed558-46c2-43ac-b328-da40ea4ec892.png)

6. Finally we got the flag!

![image](https://user-images.githubusercontent.com/70703371/180457460-12bdb6d1-80fe-47fc-b665-49c8c4394be8.png)

![decoded](https://user-images.githubusercontent.com/70703371/180457648-57a0a00a-28fc-4061-842c-1d5c7057ccc6.jpg)

---
## FLAG

```
picoCTF{beep_boop_im_in_space}
```
