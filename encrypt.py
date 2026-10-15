import random

characters = "".join(chr(i) for i in range(32,127)) + "\n"
text = input("Enter your text: ")
n = len(characters)
index = {ch: i for i,ch in enumerate(characters)}

def key_generator(length):

    return [random.randrange(n) for _ in range(length)]

def encrypt(text, key=None):

    if key is None:
        key = key_generator(len(text))
    if len(key) != len(text):
        raise ValueError("Key length must be equal to text length!")

    out = []

    for ch,dist in zip(text,key):
        if ch not in index:
            raise ValueError("Unsupported character input")
        out.append(characters[(index[ch]+dist)%n])
    return "".join(out),key

