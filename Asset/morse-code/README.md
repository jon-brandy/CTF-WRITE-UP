# morse-code
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Morse code is well known. Can you decrypt this? 
Download the file [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/d0f6516abf5314fe61b6bd02cc9b719c8ea68a75/Asset/morse-code/morse_chal.wav). Wrap your answer with picoCTF{}, put underscores in place of pauses, and use all lowercase.
## HINT:
1. Audacity is a really good program to analyze morse code audio.
## STEPS:
1. Try to use this [website](https://morsecode.world/international/decoder/audio-decoder-adaptive.html), insert the audio files there.
2. Next, click the play button and it will decode by itself.

![Screenshot (404)](https://user-images.githubusercontent.com/70703371/172411109-a497939f-529a-4786-a2d2-63c860843273.png)

3. By default, we get all the uppercase letters, but remember, based from the description we told to put underscores in place of pauses and user all lowercase.
4. So just transform the uppercase letter to lowercase and put underscores on every spaces.
5. Finally wrap the flag with `picoCTF{}`.

---

## FLAG
```
picoCTF{wh47_h47h_90d_w20u9h7}
```

