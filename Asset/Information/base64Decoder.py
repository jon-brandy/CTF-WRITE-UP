import base64
import os

os.system('cls')
strings = 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'
base64_bytes = strings.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
result = message_bytes.decode('ascii')

print(result)
