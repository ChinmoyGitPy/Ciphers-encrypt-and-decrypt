# Cipher: Encrypt and Decrypt

A small terminal app that encrypts and decrypts text messages. Each character gets shifted by a random distance and the list of shifts is the key.

## How it works

The app uses Python's `string.printable` as its alphabet i.e, 100 characters: letters, digits, punctuation, whitespace. To encrypt, it picks a random number from 0 to 99 for every character in your message and moves that character forward by that many places in the alphabet, wrapping around at the end. To decrypt, it moves each character back by the same amount.

The random numbers come from Python's `secrets` module, so they're suitable for security use. Since the key is as long as the message and every shift is independent, this works like a one-time pad. That only holds if you use a fresh key for every message and keep it secret since reusing a key makes it a lot easier to break.

## Running it

You need Python 3.9 or newer and no other dependecies.

    python cipher.py

Pick an option from the menu:

1. Encrypt: type a message and you get back a ciphertext and a key. 
2. Decrypt: paste the ciphertext with its quotes and then the key.
3. Quit.



