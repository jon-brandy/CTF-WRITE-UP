import requests
from base64 import *
from tqdm import tqdm
import os

os.system('clear')

nc = "http://mercury.picoctf.net:43275/"

sh = requests.Session()
sh.get(nc)
cookie = sh.cookies["auth_name"]
strings = b64decode(cookie)
strings2 = b64decode(strings)


def exploit():
    for position_idx in tqdm(range(0, len(strings2))):
        for bit_idx in range(0, 8):
            bitflip_guess = (
                strings2[0:position_idx]
                + ((strings2[position_idx] ^ (1 << bit_idx)).to_bytes(1, "big"))
                + strings2[position_idx + 1 :]
            )

            guess = b64encode(b64encode(bitflip_guess)).decode()
            sh = requests.get(nc, cookies={"auth_name": guess})
            if "picoCTF" in sh.text:
                print("Flag: " + sh.text.split("<code>")[1].split("</code>")[0])
                return

exploit()
