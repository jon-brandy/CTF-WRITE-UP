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
6. Based from the hint, let's open hexedit to change the header value but first convert the file to `PNG` by run -> `convert mystery mystery.png`.


