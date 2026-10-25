import ast
import secrets
import string

chars = string.printable
size = len(chars)
pos = {c: i for i, c in enumerate(chars)}


def make_key(n):
    return [secrets.randbelow(size) for _ in range(n)]


def encrypt(text):
    for c in text:
        if c not in pos:
            raise ValueError(f"can't encrypt {c!r}, it's not in the alphabet")
    key = make_key(len(text))
    result = "".join(chars[(pos[c] + shift) % size] for c, shift in zip(text, key))
    return result, key


def decrypt(text, key):
    if len(key) != len(text):
        raise ValueError("key has to be the same length as the text")
    for c in text:
        if c not in pos:
            raise ValueError(f"can't decrypt {c!r}, it's not in the alphabet")
    return "".join(chars[(pos[c] - shift) % size] for c, shift in zip(text, key))


def key_to_string(key):
    return ",".join(str(k) for k in key)


def key_from_string(s):
    try:
        return [int(x) for x in s.split(",") if x.strip()]
    except ValueError:
        raise ValueError("that key doesn't look right, it should be numbers separated by commas")


def read_cipher(raw):
    raw = raw.strip()
    try:
        value = ast.literal_eval(raw)
        if isinstance(value, str):
            return value
    except (ValueError, SyntaxError):
        pass
    return raw


def encrypt_menu():
    text = input("\nMessage: ")
    if not text:
        print("Nothing to encrypt.")
        return
    try:
        cipher, key = encrypt(text)
    except ValueError as e:
        print(e)
        return
    print("\nCiphertext:", repr(cipher))
    print("Key:", key_to_string(key))
    print("\nSave both. You can't get the message back without the key.")


def decrypt_menu():
    cipher = read_cipher(input("\nCiphertext (paste it with the quotes): "))
    try:
        key = key_from_string(input("Key: "))
        message = decrypt(cipher, key)
    except ValueError as e:
        print(e)
        return
    print("\nMessage:", message)


def main():
    print("=== Cipher ===")
    while True:
        print("\n1) Encrypt a message")
        print("2) Decrypt a message")
        print("3) Quit")
        try:
            choice = input("\n> ").strip()
            if choice == "1":
                encrypt_menu()
            elif choice == "2":
                decrypt_menu()
            elif choice == "3":
                break
            else:
                print("Pick 1, 2 or 3.")
        except (KeyboardInterrupt, EOFError):
            print()
            break


if __name__ == "__main__":
    main()