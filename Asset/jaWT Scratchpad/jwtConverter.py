import sys
from binascii import *
from jwt.utils import base64url_decode

#Function to convert jwt token to a JohnTheRipper format
def jwtConvert(token):
    # STEPS:
    # 1. Convert strings from base64 to hex
    # 2. Seperate it from the data using '#' so John can parse it
    jwtBytes = token.encode('ascii')
    parts = jwtBytes.split(b'.')
    
    data = parts[0] + b'.' + parts[1]
    strings = hexlify(base64url_decode(parts[2]))
    return (data + b'#' + strings).decode('ascii')

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: %s JWT" % sys.argv[0])
    else:
        john = jwtConvert(sys.argv[1])
        print(john)
    
