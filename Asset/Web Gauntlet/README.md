# Web Gauntlet
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
```
If the flag is not displayed after completing this challenge, try clearing your cookies. 
Cookies set by other challenges may prevent the flag from displaying properly.
```
Can you beat the filters? 
Log in as admin 
http://jupiter.challenges.picoctf.org:40791/ ,
http://jupiter.challenges.picoctf.org:40791/filter.php

## HINTS:
1. You are not allowed to login with valid credentials.
2. Write down the injections you use in case you lose your progress.
3. For some filters it may be hard to see the characters, always (always) look at the raw hex in the response.
4. sqlite
5. If your cookie keeps getting reset, try using a private browser window
## STEPS:
1. First, open the following website -> `http://jupiter.challenges.picoctf.org:41560/`.
2. Since they want us to login as `admin`, let's try to input the username and password as `admin`.

![image](https://user-images.githubusercontent.com/70703371/176408595-b96597a4-09a2-4b90-aad6-f87face817f1.png)

![image](https://user-images.githubusercontent.com/70703371/176408854-7cd077d8-e6a5-4aa1-9d32-c897ef65c0d7.png)


3. Turns out it's not that easy, let's try a sql injection by input the username as `admin'--` and the password as `admin`.

![image](https://user-images.githubusercontent.com/70703371/176409046-6abd6cfe-154a-4725-a64d-1c6f6bb2922f.png)

4.  We made it to round 2!

![image](https://user-images.githubusercontent.com/70703371/176409280-f10ff36b-b297-4806-9752-add54742e738.png)

5. Now try to input the same value as round 1.
6. Seems, it doesn't work out.

![image](https://user-images.githubusercontent.com/70703371/176409444-d6522ed4-2a8a-4fe5-871d-84d0133ef92e.png)

7. Based from the description, we can see what does the current round filtered.
8. Now try to add `/filter.php` at the url.

![image](https://user-images.githubusercontent.com/70703371/176409909-154b6d44-b621-426e-b714-cfb47b499011.png)

9. It is known that the website performs filtering on characters --, now let's try to input the username as `admin'/*` and the password as `admin`.

![image](https://user-images.githubusercontent.com/70703371/176410422-e4beef49-ae1e-4014-8ec9-28045f5da34a.png)

10. Turns out, we made it to round 3!

![image](https://user-images.githubusercontent.com/70703371/176410508-37423346-e290-46b4-b2f1-254d9ddcfbdb.png)

11. Now let's open the `filter.php` again on this round.

![image](https://user-images.githubusercontent.com/70703371/176410667-a8d16926-642e-4c50-8e35-1ad7e0af5210.png)

12. Seems, we can input the same value as round 2, because they still not filter the `/*` characters.
13. Try to input the same value as round 2.

![image](https://user-images.githubusercontent.com/70703371/176410950-88aa9a89-35f0-4fd4-8680-10750fa3a435.png)

14. We made it to round 4!

![image](https://user-images.githubusercontent.com/70703371/176411053-ed3ec962-353e-425f-9c34-c3b10ca58875.png)

15. Let's open the `filter.php` again.

![image](https://user-images.githubusercontent.com/70703371/176411229-90181f1b-5e03-491d-a96a-de2a595de67f.png)

16. It seems, we can't use the `admin` word again, and somehow we have to bypass it.
17. The easiest way to bypass it, is by using concatenation -> `||`.
18. Now, let's try to input the username as `adm'||'in` and the password as `a` or any character you want.

![image](https://user-images.githubusercontent.com/70703371/176411944-443880b1-3177-432a-bb85-7eb57d240646.png)

20. Seems, it's not work out. Let's try to comment the `'AND PASSWORD etc...`. by using the `/*`.
21. So the query will look like this:

```sql
SELECT * FROM users WHERE username='adm'||'in'/* AND password='a'
```

22. Try to input the username as `adm'||'in'/*` and the password as `a` or any character you like, because the password is gonna be a comment, so it won't give any affect.

![image](https://user-images.githubusercontent.com/70703371/176412629-2d9996ed-4658-41a0-bfda-b08dfd49c66d.png)

23. We made it to round 5!

![image](https://user-images.githubusercontent.com/70703371/176412961-fd4d42a2-b206-4b35-ad72-2a09abb0d7b2.png)

24. Next, check the `filter.php` again.

![image](https://user-images.githubusercontent.com/70703371/176413612-fe218b7e-c7b7-4bf5-b7bc-7f2e5d1963b3.png)

25. Seems, we can try to input the same value again as round 4.

![image](https://user-images.githubusercontent.com/70703371/176413761-46a00385-85b8-4a12-9bc8-c1f4c7a84125.png)

25. Now open the `filter.php` file.

![image](https://user-images.githubusercontent.com/70703371/176413881-37024471-fece-4c66-ae48-4e51b7dc261c.png)

```php
<?php
session_start();

if (!isset($_SESSION["round"])) {
    $_SESSION["round"] = 1;
}
$round = $_SESSION["round"];
$filter = array("");
$view = ($_SERVER["PHP_SELF"] == "/filter.php");

if ($round === 1) {
    $filter = array("or");
    if ($view) {
        echo "Round1: ".implode(" ", $filter)."<br/>";
    }
} else if ($round === 2) {
    $filter = array("or", "and", "like", "=", "--");
    if ($view) {
        echo "Round2: ".implode(" ", $filter)."<br/>";
    }
} else if ($round === 3) {
    $filter = array(" ", "or", "and", "=", "like", ">", "<", "--");
    // $filter = array("or", "and", "=", "like", "union", "select", "insert", "delete", "if", "else", "true", "false", "admin");
    if ($view) {
        echo "Round3: ".implode(" ", $filter)."<br/>";
    }
} else if ($round === 4) {
    $filter = array(" ", "or", "and", "=", "like", ">", "<", "--", "admin");
    // $filter = array(" ", "/**/", "--", "or", "and", "=", "like", "union", "select", "insert", "delete", "if", "else", "true", "false", "admin");
    if ($view) {
        echo "Round4: ".implode(" ", $filter)."<br/>";
    }
} else if ($round === 5) {
    $filter = array(" ", "or", "and", "=", "like", ">", "<", "--", "union", "admin");
    // $filter = array("0", "unhex", "char", "/*", "*/", "--", "or", "and", "=", "like", "union", "select", "insert", "delete", "if", "else", "true", "false", "admin");
    if ($view) {
        echo "Round5: ".implode(" ", $filter)."<br/>";
    }
} else if ($round >= 6) {
    if ($view) {
        highlight_file("filter.php");
    }
} else {
    $_SESSION["round"] = 1;
}

// picoCTF{y0u_m4d3_1t_96486d415c04a1abbbcf3a2ebe1f4d02}
?>
```

26. Finally, we got the flag!

---
## FLAG
```
picoCTF{y0u_m4d3_1t_96486d415c04a1abbbcf3a2ebe1f4d02}
```



