# like1000
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
This [.tar](https://github.com/jon-brandy/CTF-WRITE-UP/blob/642e6bcd3d5ecb293d021739e79aab8d28fb290b/Asset/like1000/1000.tar) file got tarred a lot.
## HINT:
1. Try and script this, it'll save you a lot of time.
## STEPS:
1. First, download the file given.
2. Next, try to extract the `.tar` file.
3. Then open the `1000` folder.

![image](https://user-images.githubusercontent.com/70703371/180599207-a6610f3b-3292-4b57-9486-d6fe498d334b.png)

4. Well the filter.txt file doesn't give us any clue.

![image](https://user-images.githubusercontent.com/70703371/180599321-26783f6a-8b63-4f2d-b3ea-1283d0a01372.png)

5. Then i tried to extract the `999.tar` file.

![image](https://user-images.githubusercontent.com/70703371/180599344-4ae44f91-26f2-4462-a87c-996093fa84cc.png)

6. Based from the hint we must use a script so we don't have to extract it manually and not wasting our time.
7. For this solution i used python code.

```py
import os
import tarfile

os.system("clear") 

# for loop from 1000 to 0, decrementing by 1
for i in range(1000, 0, -1): 
	filename = str(i) + '.tar' #Get the name of the file
	result = tarfile.open(filename) #Open the file
	result.extractall() # extract all the files
	result.close() #Close the file
```

8. Finally we got the last `,tar` file.

![image](https://user-images.githubusercontent.com/70703371/180599712-a55baae7-48a9-4bee-b8e6-54ca58aa787c.png)

9. Extract the file.
10. Finally we got the flag!

![image](https://user-images.githubusercontent.com/70703371/180599748-8df29493-2163-4537-bc49-2b404d5fcbed.png)


---
## FLAG

```
picoCTF{l0t5_0f_TAR5}
```
