# vault-door-1
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
This vault uses some complicated arrays! 
I hope you can make sense of it, special agent. 
The source code for this vault is here: [VaultDoor1.java]()
## HINT:
1. Look up the charAt() method online.
## STEPS:
1. First download the `.java` code.
2. Next, view the source-code.

```java
import java.util.*;

class VaultDoor1 {
    public static void main(String args[]) {
        VaultDoor1 vaultDoor = new VaultDoor1();
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

    // I came up with a more secure way to check the password without putting
    // the password itself in the source code. I think this is going to be
    // UNHACKABLE!! I hope Dr. Evil agrees...
    //
    // -Minion #8728
    public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '9' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '5' &&
               password.charAt(30) == '2' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '0' &&
               password.charAt(26) == '7' &&
               password.charAt(31) == 'e';
    }
}

```

3. I think we just need to concate every character based from the indexes start from `0`.

![image](https://user-images.githubusercontent.com/70703371/180635157-755b8e34-9c25-4f12-b329-8d92e5a2a1fb.png)

4. And wrap them around with `picoCTF{}`.

![image](https://user-images.githubusercontent.com/70703371/180635179-993bc2cc-9ecf-4d6b-a139-310a852a75f6.png)

5. Since i can't make the script, so did this manually.

> RESULT:

```
d35cr4mbl3_tH3_cH4r4cT3r5_75092e
```

6. Finally we got the flag!

---
## FLAG

```
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}
```
