# don't-use-client-side
## DESCRIPTION:
Can you break into this super secure portal? https://jupiter.challenges.picoctf.org/problem/29835/ [(link)](https://jupiter.challenges.picoctf.org/problem/29835/) or http://jupiter.challenges.picoctf.org:29835
## HINT:
1. Never trust the client
## STEPS:
1. Open the `inspect element` and see what's inside the `.html` file.
2. We can see there's unique javascript if statements there.

![Screenshot (417)](https://user-images.githubusercontent.com/70703371/172823993-05862a70-0ced-4cca-b42d-2bcdf2810eb5.png)

3. It looks like a partition of a flag.
4. Try to concate all of them in ascending order. Example -> `0, split` then `split, split*2` and so on.
5. After we concate all of them, try to submit the flag in the textarea.
6. And the website shows this pop up.

![Screenshot (418)](https://user-images.githubusercontent.com/70703371/172824779-e7513b7a-042a-4834-8ff2-5ccb17ecf728.png)


---
## FLAG:

```
picoCTF{no_clients_plz_7723ce}
```
