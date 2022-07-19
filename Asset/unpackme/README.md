# unpackme
#### Write-up author : [PlasmaRing](https://github.com/PlasmaRing)
## DESCRIPTION:
Can you get the flag?
Reverse engineer this [binary](https://github.com/jon-brandy/CTF-WRITE-UP/blob/2b72bf2ae24d76ea000d2982d6642085e0c68a31/Asset/unpackme/unpackme-upx).
## HINT:
1. What is UPX?
## STEPS:
1. Download the file
2. Checking file: `unpackme-upx` in __packed__ status using __Detect It Easy__ tool
3. Open terminal, and go to __directory file__
4. __unpack__ the file using this terminal command: `upx -d unpackme-upx -o unpackme-unpack `
5. Check the file: `unpackme-unpack` that the file successfully __unpack__
6. Open the file: `unpackme-unpack` using IDA
7. Go to `main`
8. __decompile__ the file
9. Find the __Secret Number__ : `754635`
10. Open the terminal, and go to __directory file__
11. Type `chmod +x unpackme-upx` in terminal to make file __executable__
12. Type `./unpackme-upx` to run the file
13. Input __Secret Number__ `754635`
14. Got the flag  

![PICO1](https://user-images.githubusercontent.com/92077284/160375948-f0677ea3-1887-4e6b-95f6-246b6869d41e.png)
![PICO2](https://user-images.githubusercontent.com/92077284/160375953-871b3f62-084d-4de3-b1a8-007385d58d45.png)
![PICO3](https://user-images.githubusercontent.com/92077284/160375960-44273c7a-247b-4687-ad8d-e8013ff2416a.png)
![PICO4](https://user-images.githubusercontent.com/92077284/160375969-25b2803f-8d62-4578-bc51-20c555b5ec6f.png)
![PICO5](https://user-images.githubusercontent.com/92077284/160375976-1fd629cb-b192-4dfe-b947-5a3bec824791.png)
![PICO6](https://user-images.githubusercontent.com/92077284/160375980-8cd62bcc-5ea5-48f6-bb04-e576ed47930d.png)
---

## FLAG
```
picoCTF{up><_m3_f7w_a6870b23}
```
