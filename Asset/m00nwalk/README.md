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

4. It is known there's a tool at kali linux called **qsstv**.

> INSTALLATION

```
sudo apt-get install qsstv
```

6. Now let's open `qsstv` at kali linux by run this command at the terminal:

```
qsstv 
```

7. Next, choose `options` then choose `configuration`.

![image](https://user-images.githubusercontent.com/70703371/180446557-1e4453c4-fe09-4251-a7cd-384547859974.png)

8. Then choose `sound` and select the `PulseAudio`.

![image](https://user-images.githubusercontent.com/70703371/180446735-0af22be3-9293-4dcd-ae6d-958601aaf75d.png)

9. 
