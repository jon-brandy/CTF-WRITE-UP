# Forbidden Paths
## DESCRIPTION:
Can you get the flag? Here's the [website](http://saturn.picoctf.net:55827/). 
We know that the website files live in `/usr/share/nginx/html/`and the flag is at /flag.txt but the website is filtering absolute file paths. 
Can you get past the filter to read the flag?
## HINT:
- NONE
## STEPS:
1. Click the website link.
2. Based from the description, try to input `usr/share/nginx/html/flag.txt`.

![Screenshot (502)](https://user-images.githubusercontent.com/70703371/176099066-0fd73d9e-3fce-42b1-bde9-706b550be6ea.png)

3. Seems we don't get the flag.
4. Next, if you read the description carefully, you will realize that the absolute file paths are filtered, so try to input like this `../../../../flag.txt`.
