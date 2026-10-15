import random

characters = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g',
              'h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0',' ']

text = input("Enter your text: ")
n = len(text)


def key_generator(n=n):

    return [random.randrange(63) for _ in range(n)]

for t in text:
    if t not in characters:
        print("Unsupported Characters: Please use numbers,alphabets and space only")
    else:
        print(key_generator())