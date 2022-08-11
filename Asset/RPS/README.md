# RPS
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Here's a program that plays rock, paper, scissors against you. I hear something good happens if you win 5 times in a row. 
Connect to the program with netcat: `$ nc saturn.picoctf.net 56981`
The program's source code with the flag redacted can be downloaded [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/497d6314d758e3272dd8884d155e91921227af37/Asset/RPS/game-redacted.c).
## HINT:
1. How does the program check if you won?
## STEPS:
1. First, download the file given.
2. Now let's analyze the `.c` code.
3. It seems we need to win the game **5 times** so we can have the flag.

![image](https://user-images.githubusercontent.com/70703371/184157763-dbc48bda-370a-4c70-94b3-54396badb333.png)

4. Let's check the `play` function here.

![image](https://user-images.githubusercontent.com/70703371/184157906-ceb4f66c-5cc4-4f70-aedc-5a7603746d32.png)

> PLAY FUNCTION

```c
bool play () {
  char player_turn[100];
  srand(time(0));
  int r;

  printf("Please make your selection (rock/paper/scissors):\n");
  r = tgetinput(player_turn, 100);
  // Timeout on user input
  if(r == -3)
  {
    printf("Goodbye!\n");
    exit(0);
  }

  int computer_turn = rand() % 3;
  printf("You played: %s\n", player_turn);
  printf("The computer played: %s\n", hands[computer_turn]);

  if (strstr(player_turn, loses[computer_turn])) {
    puts("You win! Play again?");
    return true;
  } else {
    puts("Seems like you didn't win this time. Play again?");
    return false;
  }
}
```

5. If we bruteforced it, we may never win.
6. Seems they also have some kind of dictionary.

![image](https://user-images.githubusercontent.com/70703371/184161098-2a40ccac-0b92-421d-82e8-3dad82e9251c.png)

7. Notice here, they don't specify the input.

![image](https://user-images.githubusercontent.com/70703371/184160208-5c2f823a-43c6-423e-8872-e45b46e2a3ef.png)

8. Therefore to trick the computer, i tried to input `paperscissorsrock`.

![image](https://user-images.githubusercontent.com/70703371/184161218-973fa324-6414-4d6d-ba39-81b8f90b923d.png)

9. Well it does work, let's try it again!

![image](https://user-images.githubusercontent.com/70703371/184161330-a79f0f40-3ea9-441b-a66b-80d57bdfe4fb.png)

10. Seems this is the vuln.
11. At the final game, i won and got the flag!

![image](https://user-images.githubusercontent.com/70703371/184161441-1eb04506-2709-4857-8f83-2c2c9222fdce.png)


---

## FLAG

```
picoCTF{50M3_3X7R3M3_1UCK_C85AF58A}
```
