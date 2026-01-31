from pprint import pprint

from aes import encrypt_aes, decrypt_aes

example_text = """
PyCryptodome is a self-contained Python package of low-level cryptographic primitives.
It is a fork of the popular cryptography library, Cryptodome, which is a fork of the popular cryptography library, Cryptography.
It supports Python 2.7, Python 3.7 and newer, and PyPy.
"""
key = 517
key = str(key).encode()
cipher_text = encrypt_aes(example_text, key)

print('\n1:')
pprint(cipher_text)

# print('\n2:')
# result_text = decrypt_aes(cipher_text, key)
# pprint(result_text.decode("utf-8"))

for candidate_key in range(0, 999):
    candidate_key = str(candidate_key).encode()
    try:
        pt = decrypt_aes(cipher_text, candidate_key)
        text = pt.decode("utf-8")
        if "PyCryptodome" in text:
            print("key:", candidate_key)
            print("text:", text)
            break
    except Exception:
        pass

