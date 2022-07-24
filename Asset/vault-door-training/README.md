# vault-door-training
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. 
The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. 
Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, 
but one of our junior agents obtained the source code for each vault's computer! 
You will need to read the source code for each level to figure out what the password is for that vault door. 
As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](https://github.com/jon-brandy/CTF-WRITE-UP/blob/4ced07115e9fad9c65ff2715e101c0fac7a23c54/Asset/vault-door-training/VaultDoorTraining.java)
## HINT:
1. The password is revealed in the program's source code.
## STEPS:
1. First, download the file given.
2. Based from the hint, we should view the source-code.

```java
import java.util.*;

class VaultDoorTraining {
    public static void main(String args[]) {
        VaultDoorTraining vaultDoor = new VaultDoorTraining();
        Scanner scanner = new Scanner(System.in); 
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
	}
   }

    // The password is below. Is it safe to put the password in the source code?
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security
    // on the other doors.
    //
    // -Minion #9567
    public boolean checkPassword(String password) {
        return password.equals("w4rm1ng_Up_w1tH_jAv4_be8d9806f18");
    }
}

```

3. Wrap this strings with `picoCTF{}`.

![image](https://user-images.githubusercontent.com/70703371/180634908-d8b4a42a-2b1b-4652-9922-fccd756eef32.png)

4. We already got the flag then!

---
## FLAG

```
picoCTF{w4rm1ng_Up_w1tH_jAv4_be8d9806f18}
```
