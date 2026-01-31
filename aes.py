import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto import Random
from pprint import pprint

def encrypt_aes(example_text: bytes, key: str) -> bytes:
    key = hashlib.sha256(key).digest()
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * bytes([BS - len(s) % BS])
    plain_text = pad(example_text.encode())
    iv = Random.new().read(BS)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = (iv + cipher.encrypt(plain_text))
    return cipher_text

def decrypt_aes(cipher_text: bytes, key: str) -> bytes:
    key = hashlib.sha256(key).digest()
    BS = AES.block_size
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]
    iv = cipher_text[:BS]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    result_text = unpad(cipher.decrypt(cipher_text[BS:]))
    return result_text