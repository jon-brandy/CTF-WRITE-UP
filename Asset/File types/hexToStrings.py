import os

os.system("cls")

strings = "7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f6630725f3062326375723137795f39353063346665657d0a"
result = bytearray.fromhex(strings)
fin = result.decode()
print(fin)
