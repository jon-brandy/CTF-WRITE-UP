# Includes
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Can you get the flag?
Go to this [website](http://saturn.picoctf.net:57833) and see what you can discover.
## HINT:
1. Is there more code than what the inspector initially shows?
## STEPS:
1. First, try to see the source code of the website by opening the inspect element.
2. On the `.css` file, there is a flag at the comment line:
```css
body {
  background-color: lightblue;
}

/*  picoCTF{1nclu51v17y_1of2_  */
```
3. Next, try to open the `.js` file, there is a flag at the comment line too.
```js
function greetings()
{
  alert("This code is in a separate file!");
}

//  f7w_2of2_b8f4b022}
```
4. Last, just concate all the strings.
5. Finally we have the complete flag!


---

## FLAG
```
picoCTF{1nclu51v17y_1of2_f7w_2of2_b8f4b022}
```
