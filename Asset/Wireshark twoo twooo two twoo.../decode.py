import base64
import os

os.system('cls')
strings = 'cGljb0NURntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ=='
base64_bytes = strings.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
result = message_bytes.decode('ascii')

print(result)
