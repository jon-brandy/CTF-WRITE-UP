# file-run2
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Another program, but this time, it seems to want some input. 
What happens if you try to run it on the command line with input "Hello!"? 
Download the program [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/d1deee62b2cb4de7de32842857e4d7131a97afea/Asset/file-run2/run).
## HINT:
1. Try running it and add the phrase "Hello!" with a space in front (i.e. "./run Hello!")
## STEPS:
1. First, download the file given.
2. Based from the hint, let's try to run this command `./run Hello!`

![Screenshot (466)](https://user-images.githubusercontent.com/70703371/175036605-88d03c02-724a-4a02-b78c-3a4eed26c287.png)

3. Turns out we don't have permission to run the file.
4. Now search the file at your directory, then right click and choose `properties`.
5. Now tick "Allow this file to run as a program".

![Screenshot (467)](https://user-images.githubusercontent.com/70703371/175037199-15ff9196-76e7-49de-bcad-d09d30787b2e.png)

6. Then open your kali linux terminal and type the same command again -> `./run Hello!`.

![Screenshot (468)](https://user-images.githubusercontent.com/70703371/175037630-d0bfc86e-eeb4-4e0f-b5b2-e273a9fa13cd.png)

7. Finally we got the flag!


---
## FLAG
```
picoCTF{F1r57_4rgum3n7_f65ed63e}
```
