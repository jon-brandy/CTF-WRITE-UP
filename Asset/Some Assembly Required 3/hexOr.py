import os

os.system('clear')

hexa1024 = "\x9dn\x93\xc8\xb2\xb9A\x8b\xc2\x97\xd4f\xc7\x93\xc4\xd4a\xc2\xc6\xc9\xddb\x94\x9e\xc2\x892\x91\x90\xc1\xdd3\x91\x91\x97\x8bd\xc1\x92\xc4\x90\x00\x00"
hexa1067= "\xf1\xa7\xf0\x07\xed"

for i in range(len(hexa1024)):
    print(chr(ord(hexa1024[i])^ord(hexa1067[4 - (i % 5)])), end="")