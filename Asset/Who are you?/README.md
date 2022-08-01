# Who are you?
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn 
http://mercury.picoctf.net:34588/
## HINT:
1. It ain't much, but it's an RFC https://tools.ietf.org/html/rfc2616
## STEPS:
1. First, open the link given.

![image](https://user-images.githubusercontent.com/70703371/182081010-82b3b6c2-355c-4310-84c7-588f05c1c680.png)

2. Seems we have to change the `user-agent` value.
3. For this solution i used `burpsuite`. So i paste the url using `burpsuite` browser.

> CHOOSE SEND TO REPEATER

![image](https://user-images.githubusercontent.com/70703371/182081571-109120dc-b5c2-438d-af16-00cf88ffa9cc.png)

> OPEN REPEATER TAB CLICK THE SEND BUTTON

![image](https://user-images.githubusercontent.com/70703371/182081623-6d47c5d2-3e70-436a-9769-187d65d1b82a.png)

4. Change the `user-agent` value to `PicoBrowser` then click the `send` button again.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182081891-1f304a8d-a0c5-4605-9584-329e5117a5ee.png)

5. The clue here is `from another site`, means we may have to add a header called `Referer` and input the url from the description as it's value, then press the `send` button.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182082840-c3d0f4c3-df58-418c-9a7c-56a05b1cf810.png)

6. Seems we are making new progress.
7. `Only worked in 2018` means we may have to add a new header again called `Date`.
8. Now add `Date: Mon, 1 Jan 2018 01:00:00 GMT` then press the `send` button.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182083191-ed04d5be-f8be-413d-b5b5-16c77b849c9a.png)

9. We're doing great so far.
10. `i don't trust users who can be tracked` means we must add `DNT` header and input the value as `1` (true).

> NOTES & RESEARCH LINK

```
Do Not Track (DNT) is a browser setting that sends a message to websites and advertising networks requesting that they don't track the user. Firefox, Internet Explorer and Safari provide DNT settings.

https://www.techtarget.com/whatis/definition/Do-Not-Track-DNT
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182083664-55ef45c6-4b71-434d-939c-85d86b2d5a5b.png)

12. `Is only for people from Sweden` means we have to change our IP.
13. Now add a header called `X-Forwarded-For` and input the value as `1.208.107.42`

> RESEARCH LINK

```
https://en.wikipedia.org/wiki/X-Forwarded-For
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For
https://lite.ip2location.com/sweden-ip-address-ranges?lang=en_US
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182092086-82bb8382-b677-4d88-94a6-4503e14146f4.png)

14. `don't speak swedish` means we must change the `accept-language` value to `sv-SE` (swedish-sweden), then click the `send` button.

> RESEARCH LINK

```
http://www.lingoes.net/en/translator/langcode.htm
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182092459-75a59929-cdda-4acf-a03b-c936217f7224.png)

15. Finally, we got the flag!
16. Choose the `raw` tab to copy the flag easily.

```html
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 1062

<!DOCTYPE html>
<html lang="en">

<head>
    <title>Who are you?</title>


    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">

    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>


</head>

<body>

    <div class="container">
      <div class="jumbotron">
        <p class="lead"></p>
		<div class="row">
			<div class="col-xs-12 col-sm-12 col-md-12">
				<h3 style="color:green">What can I say except, you are welcome</h3>
			</div>
		</div>
		<br/>
		
			<b>picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_79e451a7}</b>
		
	</div>
    <footer class="footer">
        <p>&copy; PicoCTF</p>
    </footer>

</div>
<script>
$(document).ready(function(){
    $(".close").click(function(){
        $("myAlert").alert("close");
    });
});
</script>
</body>

</html>
```
---

## FLAG

```
picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_79e451a7}
```


## REFERENCES

```
http://www.lingoes.net/en/translator/langcode.htm
https://www.techtarget.com/whatis/definition/Do-Not-Track-DNT
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For
https://en.wikipedia.org/wiki/X-Forwarded-For
https://lite.ip2location.com/sweden-ip-address-ranges?lang=en_US
```
