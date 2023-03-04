from pwn import *
import os

os.system('cls')

expected_value = '4a53475d414503545d025a0a5357450d05005d555410010e4155574b45504601'
key = '861836f13e3d627dfa375bdb8389214e'

getPlain = xor(unhex(expected_value),key)
info('Plain text: %s', getPlain)
