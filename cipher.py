import secrets
import string

chars = string.printable
size = len(chars)
pos = {c: i for i, c in enumerate(chars)}


def make_key(n):
    return [secrets.randbelow(size) for _ in range(n)]


def encrypt(text, key=None):
    if key is None:
        key = make_key(len(text))
    if len(key) != len(text):
        raise ValueError("key has to be the same length as the text")

    result = ""
    for c, shift in zip(text, key):
        if c not in pos:
            raise ValueError(f"can't encrypt {c!r}, it's not in the alphabet")
        result += chars[(pos[c] + shift) % size]
    return result, key


def decrypt(text, key):
    if len(key) != len(text):
        raise ValueError("key has to be the same length as the text")

    result = ""
    for c, shift in zip(text, key):
        if c not in pos:
            raise ValueError(f"can't decrypt {c!r}, it's not in the alphabet")
        result += chars[(pos[c] - shift) % size]
    return result


def key_to_string(key):
    return ",".join(str(k) for k in key)


def key_from_string(s):
    return [int(x) for x in s.split(",") if x.strip()]


if __name__ == "__main__":
    message = input("Message to encrypt: ")
    cipher, key = encrypt(message)

    print("\nCiphertext:", repr(cipher))
    print("Key:", key_to_string(key))

    restored = decrypt(cipher, key_from_string(key_to_string(key)))
    print("Decrypted:", restored)
    assert restored == message, "round trip failed"
     
