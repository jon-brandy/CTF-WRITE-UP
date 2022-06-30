# Fresh Java
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Can you get the flag? 
Reverse engineer this [java program](https://github.com/jon-brandy/CTF-WRITE-UP/blob/24876e2363024bc762f1f4fab33d38f7a1fe3120/Asset/Fresh%20Java/KeygenMe.class).
## HINT:
1. Use a decompiler for Java!
## STEPS:
1. First, download the file given.
2. Next, based from the hint, we must use java decompiler, to get the `.java` source code.
3. For this solution i used [online decompiler](http://www.javadecompilers.com/). Input the `.class` file, then click the `Upload and Decompile` button.
4. Then, we got the zipped file.

![image](https://user-images.githubusercontent.com/70703371/176596522-b8cf04b4-14b0-423e-95bf-4a8f3a880674.png)

5. After you download the file, extract the file.
6. We got the `keygenMe.java` file.

```java
import java.util.Scanner;

// 
// Decompiled by Procyon v0.5.36
// 

public class KeygenMe
{
    public static void main(final String[] array) {
        final Scanner scanner = new Scanner(System.in);
        System.out.println("Enter key:");
        final String nextLine = scanner.nextLine();
        if (nextLine.length() != 34) {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(33) != '}') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(32) != 'd') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(31) != '0') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(30) != 'a') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(29) != '1') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(28) != 'e') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(27) != 'f') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(26) != 'b') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(25) != '2') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(24) != '_') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(23) != 'd') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(22) != '3') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(21) != 'r') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(20) != '1') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(19) != 'u') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(18) != 'q') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(17) != '3') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(16) != 'r') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(15) != '_') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(14) != 'g') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(13) != 'n') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(12) != '1') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(11) != 'l') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(10) != '0') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(9) != '0') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(8) != '7') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(7) != '{') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(6) != 'F') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(5) != 'T') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(4) != 'C') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(3) != 'o') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(2) != 'c') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(1) != 'i') {
            System.out.println("Invalid key");
            return;
        }
        if (nextLine.charAt(0) != 'p') {
            System.out.println("Invalid key");
            return;
        }
        System.out.println("Valid key");
    }
}

```
