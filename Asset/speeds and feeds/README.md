# speeds and feeds
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
There is something on my shop network running at `nc mercury.picoctf.net 33596`, but I can't tell what it is. Can you?
## HINT:
1. What language does a CNC machine use?
## STEPS:
1. Run the netcat given.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/189484803-4c267cc1-4f21-4941-9426-1b2f38c04299.png)

2. Based from the hint, it is a **G-Code**. [G-Code](https://github.com/jon-brandy/CTF-WRITE-UP/blob/e45052a172d558129a3b232fb8e799caf5a5466e/Asset/speeds%20and%20feeds/nc.gcode)


![image](https://user-images.githubusercontent.com/70703371/189485041-7035fce6-4630-4775-bc86-19d5438d92b4.png)


3. Simply using [this](https://ncviewer.com/) online tools, which can read gcode.
4. Paste the gcode at the new file and click the `plot` button.

![image](https://user-images.githubusercontent.com/70703371/189485094-2575d234-25bd-49c3-b610-d83e53bd9048.png)


5. Finally, we got the flag!

## FLAG

```
picoCTF{num3r1cal_c0ntr0l_e7749028}
```

## LEARNING REFERENCES

```
https://www.fictiv.com/articles/g-code-knowledge-is-key-to-mastering-any-cnc-machine
```



