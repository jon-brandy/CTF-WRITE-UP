# c0rrupt
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
We found this [file](https://github.com/jon-brandy/CTF-WRITE-UP/blob/a157f557d9130bf8326dc49335b55a97453d4907/Asset/c0rrupt/mystery). Recover the flag.
## HINT:
1. Try fixing the file header
## STEPS:
1. First, download the file given.
2. Next, let's check the file type by run -> `file mystery`.

![image](https://user-images.githubusercontent.com/70703371/180592421-3b7e1d6e-0add-41ba-a2df-1d8a25e1cd6f.png)

3. Seems, we got no clue, then i tried to run `strings mystery`.
4. At the bottom line, there's a string that caught my attention.

![image](https://user-images.githubusercontent.com/70703371/180592451-4756cf6e-1a97-47c8-bdb5-fc69a4f53629.png)

5. I think it might be a `PNG` file.
6. Let's convert the file to `PNG` by run -> `convert mystery mystery.png`.

![image](https://user-images.githubusercontent.com/70703371/180592498-1cdb738a-7d28-41d6-8b05-b9f649ec870d.png)

7. Well it gave us a clue, which means we need to change the header file by open a hexeditor.
8. For this solution, i download a `.png` file first and open it on a hexeditor to see the header value. So that we can paste it at the `mystery` file's header.

> IMAGE I DOWNLOAD:

[RANDOM PNG IMAGE FROM THE INTERNET](https://user-images.githubusercontent.com/70703371/180592570-7fd26f04-5445-466e-a502-dc81a1f81a25.png)

> HEXEDITOR OUTPUT AND VALUE WE NEED TO COPY:

![image](https://user-images.githubusercontent.com/70703371/180592685-8e1ac720-9208-4d80-8c89-8aa187ed4d7c.png)

![image](https://user-images.githubusercontent.com/70703371/180598592-9711e626-004e-44d2-bbae-ac947194a386.png)

> VALUE CHANGED AT THE MYSTERY FILE:

![image](https://user-images.githubusercontent.com/70703371/180592681-9ca595fd-ed8e-4cd9-a838-2ce51d95e946.png)

![image](https://user-images.githubusercontent.com/70703371/180598625-9c3f6932-1804-4b66-9bd6-58e452191c71.png)

9. Now, let's open the image file by adding `.png` at the end of the file.

![image](https://user-images.githubusercontent.com/70703371/180598722-a4d09727-31f9-4e49-843e-c3ca6c7f2d25.png)

10. Finally we got the flag!

---
## FLAG

```
picoCTF{c0rrupt10n_1847995}
```



