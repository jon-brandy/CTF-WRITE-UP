# JAuth
> Write-up author: vreshco
## DESCRIPTION:
Most web application developers use third party components without testing their security. Some of the past affected companies are:

    Equifax (a US credit bureau organization) - breach due to unpatched Apache Struts web framework CVE-2017-5638
    Mossack Fonesca (Panama Papers law firm) breach - unpatched version of Drupal CMS used
    VerticalScope (internet media company) - outdated version of vBulletin forum software used

Can you identify the components and exploit the vulnerable one? The website is running here. Can you become an admin? You can login as test with the password Test123! to get started.

## HINT:
1. Use the web browser tools to check out the JWT cookie.
2. The JWT should always have two (2) . separators.
## STEPS:
1. First open the link given.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/217517687-f4ff83aa-6647-4d30-81a7-b19ee537a89a.png)


2. Since there's no register button, we can use the creds given at the description.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/217517849-f9bf601a-4c79-4073-980c-15e6de188205.png)


3. Clearly nothing to see here, let's get the token.

> RESULT

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdXRoIjoxNjc1ODU1ODMyNjczLCJhZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwOS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwOS4wIiwicm9sZSI6InVzZXIiLCJpYXQiOjE2NzU4NTU4MzN9.hmtzP0PqB8HlJ4NbO6uffs3dc7TE2m64Bbsu8Df6T9o
```

4. Decode that using [this](https://jwt.io/) online tool.

![image](https://user-images.githubusercontent.com/70703371/217518206-7b7bfb11-15bc-4a1b-8801-9da8cd12dade.png)


5. Let's try with the simple approach by changing the role value to "admin", then copy the encoded jwt token then paste it in to the webapp as our token.


![image](https://user-images.githubusercontent.com/70703371/217518865-5963193a-79d6-4c1d-b5c9-317c699b7f1b.png)


> RESULT

![image](https://user-images.githubusercontent.com/70703371/217519131-fe059eb7-2413-46b1-8c6f-692b1a2bdb01.png)


6. Hmm.. we can use another approach by remove the algorithm used, we can change it to **none**. But since jwt.io can change the alg to none, because it's not in the database, we can use [this](https://token.dev/) jwt debugger.

> CHANGE IT TO NONE

![image](https://user-images.githubusercontent.com/70703371/217521278-b0686d36-6fbe-4b7f-b433-0eb42342f610.png)


```
eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdXRoIjoxNjc1ODU1ODMyNjczLCJhZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwOS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwOS4wIiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNjc1ODU1ODMzfQ
```

7. Now login again as `test`, then after paste the token, remember jwt always have 2 dots (.), while we have one, let's add another dot at the end.

> FINAL TOKEN

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdXRoIjoxNjc1ODU1ODMyNjczLCJhZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwOS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwOS4wIiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNjc1ODU1ODMzfQ.
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/217522272-59229211-fcf8-4c54-8016-50330268c19f.png)


8. Got the flag!

## FLAG

```
picoCTF{succ3ss_@u7h3nt1c@710n_bc6d9041}
```


