# Search Source
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
The developer of this website mistakenly left an important artifact in the website source, can you find it?
The website is [here](http://saturn.picoctf.net:61941)
## HINT:
1. How could you mirror the website on your local machine so you could use more powerful tools for searching?
## STEPS:
1. First, open the inspect element.
2. Next, try to open the source code of the website.
3. After opened several source code, the flag found inside the `style.css` document, at the line 328. There is a comment like this:
```
/** banner_main picoCTF{1nsp3ti0n_0f_w3bpag3s_8de925a7} **/
```
4. So we already found the flag!

---

## FLAG
```
picoCTF{1nsp3ti0n_0f_w3bpag3s_8de925a7}
```

