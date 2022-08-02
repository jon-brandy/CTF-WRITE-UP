# SideChannel
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag? 
Download the PIN checker program here [pin_checker](). Once you've figured out the PIN (and gotten the checker program to accept it), 
connect to the master server using nc saturn.picoctf.net 52680 and provide it the PIN to get your flag.
## HINTS:
1. Read about "timing-based side-channel attacks."
2. Attempting to reverse-engineer or exploit the binary won't help you, you can figure out the PIN just by interacting with it and measuring certain properties about it.
3. Don't run your attacks against the master server, it is secured against them. The PIN code you get from the `pin_checker` binary is the same as the one for the master server.
## STEPS:
1. First, download the PIN checker program.

> SOURCE-CODE

