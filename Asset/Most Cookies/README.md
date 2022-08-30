# Most Cookies
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Alright, enough of using my own encryption. 
Flask session cookies should be plenty secure! [server.py](https://github.com/jon-brandy/CTF-WRITE-UP/blob/469ad6719d39b72c023ca8cc34b13f6494269572/Asset/Most%20Cookies/server.py) http://mercury.picoctf.net:6259/
## HINT:
1. How secure is a flask cookie?
## STEPS:
1. First, open the link given.
2. Next, let's view the python script given.

```py
from flask import Flask, render_template, request, url_for, redirect, make_response, flash, session
import random
app = Flask(__name__)
flag_value = open("./flag").read().rstrip()
title = "Most Cookies"
cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]
app.secret_key = random.choice(cookie_names)

@app.route("/")
def main():
	if session.get("very_auth"):
		check = session["very_auth"]
		if check == "blank":
			return render_template("index.html", title=title)
		else:
			return make_response(redirect("/display"))
	else:
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

@app.route("/search", methods=["GET", "POST"])
def search():
	if "name" in request.form and request.form["name"] in cookie_names:
		resp = make_response(redirect("/display"))
		session["very_auth"] = request.form["name"]
		return resp
	else:
		message = "That doesn't appear to be a valid cookie."
		category = "danger"
		flash(message, category)
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

@app.route("/reset")
def reset():
	resp = make_response(redirect("/"))
	session.pop("very_auth", None)
	return resp

@app.route("/display", methods=["GET"])
def flag():
	if session.get("very_auth"):
		check = session["very_auth"]
		if check == "admin":
			resp = make_response(render_template("flag.html", value=flag_value, title=title))
			return resp
		flash("That is a cookie! Not very special though...", "success")
		return render_template("not-flag.html", title=title, cookie_name=session["very_auth"])
	else:
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

if __name__ == "__main__":
	app.run()


```

3. The flag function caught my attention.

![image](https://user-images.githubusercontent.com/70703371/187353237-36cb47ba-274e-44c6-bbd9-3789dde7554b.png)

4. Seems we need to store these values in the cookie -> `{"very_auth":"admin"}`.
5. Also this lists of cookies.

![image](https://user-images.githubusercontent.com/70703371/187353729-fdfc324d-3fce-4b05-9e96-d76dab12e3e9.png)

6. So i used this script to automatically submit each string from the wordlist.

```py

```


