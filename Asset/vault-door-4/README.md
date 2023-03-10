# vault-door-4
> Write-up author: jon-brandy
## DESCRIPTION:
This vault uses ASCII encoding for the password. The source code for this vault is here: VaultDoor4.java
## HINT:
1. Use a search engine to find an "ASCII table".
2. You will also need to know the difference between octal, decimal, and hexadecimal numbers.
## STEPS:
1. Given a java source-code, let's analyze it then.

```java
import java.util.*;

class VaultDoor4 {
    public static void main(String args[]) {
        VaultDoor4 vaultDoor = new VaultDoor4();
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

    // I made myself dizzy converting all of these numbers into different bases,
    // so I just *know* that this vault will be impenetrable. This will make Dr.
    // Evil like me better than all of the other minions--especially Minion
    // #5620--I just know it!
    //
    //  .:::.   .:::.
    // :::::::.:::::::
    // :::::::::::::::
    // ':::::::::::::'
    //   ':::::::::'
    //     ':::::'
    //       ':'
    // -Minion #7781
    public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 070 , 0146,
            '4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
}

```

2. At the main function we know that our input shall validated by calling the `checkPassword()` function.
3. Inside the myBytes variable we know that there are 3 encoded text, namely ascii code, hex, and octal.
4. Decode all of them then concate it, including the **4a6cbf3b**, shall gave us the flag!
5. Wrap it with picoCTF{}.
6. To check whether our flag is correct or not, simply run the program then input the flag.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/224357267-4b3b5a9f-af8a-4f08-8aa5-a4597dedd7cb.png)



## FLAG

```
picoCTF{jU5t_4_bUnCh_0f_bYt3s_8f4a6cbf3b}
```



