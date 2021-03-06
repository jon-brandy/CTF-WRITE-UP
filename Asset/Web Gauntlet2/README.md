# Web Gauntlet 2
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
```
If the flag is not displayed after completing this challenge, try clearing your cookies. 
Cookies set by other challenges may prevent the flag from displaying properly.
```
This website looks familiar... 
Log in as admin Site: http://mercury.picoctf.net:57359/ Filter: http://mercury.picoctf.net:57359/filter.php
## HINTS:
1. I tried to make it a little bit less contrived since the mini competition.
2. Each filter is separated by a space. Spaces are not filtered.
3. There is only 1 round this time, when you beat it the flag will be in filter.php.
4. There is a length component now.
5. sqlite
## STEPS:
1. First, open the website -> `http://mercury.picoctf.net:57359/`.
2. Try to input the user as `admin` and password as `admin`, then click `sign in`.

![image](https://user-images.githubusercontent.com/70703371/176359524-bab1d32f-97e3-4980-877b-5a5bded8da4e.png)

3. It said `filtered`.

![image](https://user-images.githubusercontent.com/70703371/176359641-89709f85-be71-4337-92db-4076df442cf4.png)

4. Now try to open the `http://mercury.picoctf.net:57359/filter.php`.

![image](https://user-images.githubusercontent.com/70703371/176359789-e76bcf1f-3ae7-4b37-9442-4a0a219dfc61.png)

5. We can conclude that the website does filter few entities.
6. Next, let's try to input the unfiltered word, in this case i tried to input `user` as username and `pass` as password.

![image](https://user-images.githubusercontent.com/70703371/176362401-8ebc806b-c876-4a01-9b8b-4461cef2d38f.png)

7. It said `not admin`. Means we must use the username as `admin` but we need to bypass it. 

![image](https://user-images.githubusercontent.com/70703371/176362494-61d82bab-62a9-427c-9241-39ac94184a14.png)

8. Since concatenation is not prohibited, then the easiest bypass is to use `||` for concatenation at the username. Now input `ad'||'min` as username and `pass` as password.
9. It still gave us a response -> `not admin`.

![image](https://user-images.githubusercontent.com/70703371/176363397-4219e66a-2ede-4fc6-afc3-7a7e45438b1c.png)

10. Now let's remodel this query: 

![image](https://user-images.githubusercontent.com/70703371/176363696-8d5a7d8c-51b9-41e3-8c43-01709c3b3920.png)

11. Change the query to this:

```sql
SELECT username, password FROM users WHERE username='ad'||'min'||substr(' AND password=',0,0)||''
```

12. Based from the query, we fill the username as `ad'||'min'||substr(` and the password as `,0,0)||'`.

![image](https://user-images.githubusercontent.com/70703371/176365185-ec7b4757-f7c2-4417-a114-ab2bec0ab1cc.png)

![image](https://user-images.githubusercontent.com/70703371/176365225-1b6fb033-0272-4e1a-92ea-8102ae4c14de.png)

13. Now open the `filter.php` file. Finally we got the flag!

![image](https://user-images.githubusercontent.com/70703371/176365402-1e03e4ae-ed40-404e-bb32-165e0dbe4bc7.png)

> ALTERNATE SOLUTIONS (USING SQLite)

1. If you want to use sqlite, for username still using concatenation -> `ad'||'min`. For the password you can use the SQLite logical property -> `IS NOT`.

![image](https://user-images.githubusercontent.com/70703371/176365789-a99929e7-68bb-43bd-86d6-25c5b8e1fe8f.png)

2. Now input the username as `ad'||'min` and the password as `a' IS NOT 'b`.

![image](https://user-images.githubusercontent.com/70703371/176366084-03cec152-c7dd-4e59-a6f4-6bb94db99602.png)

![image](https://user-images.githubusercontent.com/70703371/176366143-aa18211f-34b8-4d40-9db4-ed189f2319c3.png)

```php
<?php
session_start();

if (!isset($_SESSION["winner2"])) {
    $_SESSION["winner2"] = 0;
}
$win = $_SESSION["winner2"];
$view = ($_SERVER["PHP_SELF"] == "/filter.php");

if ($win === 0) {
    $filter = array("or", "and", "true", "false", "union", "like", "=", ">", "<", ";", "--", "/*", "*/", "admin");
    if ($view) {
        echo "Filters: ".implode(" ", $filter)."<br/>";
    }
} else if ($win === 1) {
    if ($view) {
        highlight_file("filter.php");
    }
    $_SESSION["winner2"] = 0;        // <- Don't refresh!
} else {
    $_SESSION["winner2"] = 0;
}

// picoCTF{0n3_m0r3_t1m3_d5a91d8c2ae4ce567c2e8b8453305565}
?>
```

## REFERENCES:
> SQLite CheatSheet
```
https://www.tutorialspoint.com/sqlite/sqlite_operators.htm
```

---

## FLAG
```
picoCTF{0n3_m0r3_t1m3_d5a91d8c2ae4ce567c2e8b8453305565}
```




