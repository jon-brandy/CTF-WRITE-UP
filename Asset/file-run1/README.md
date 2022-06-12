# file-run1
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
A program has been provided to you, 
what happens if you try to run it on the command line?
Download the program [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/54bc50b2a2e3191c41966dc8d71b9bbed5375ca3/Asset/file-run1/run).
## HINTS:
1. To run the program at all, you must make it executable `(i.e. $ chmod +x run)`.
2. Try running it by adding a '.' in front of the path to the file `(i.e. $ ./run)`.
## STEPS:
1. First, download the program given.
2. Next, open your terminal and type this command `chmod +x run` in order to make the program executeable.

![Screenshot (119)](https://user-images.githubusercontent.com/70703371/173182970-a4ef154a-b867-43ad-9d5e-c987ef90bb2a.png)

4. Then, if you try to run `ls` on the same folder you stored the program. You can see `run` program color file changed to green, which means it's executeable.

![Screenshot (120)](https://user-images.githubusercontent.com/70703371/173183012-d846f210-0f1d-4d57-80ec-72077d320a55.png)

4. Now, run the program using `./run` command.

![Screenshot (118)](https://user-images.githubusercontent.com/70703371/173183021-17306c53-4718-4260-a5e3-73fa745d8221.png)

5. Finally, we got the flag!


---


## FLAG:
```
picoCTF{U51N6_Y0Ur_F1r57_F113_47cf2b7b}
```
