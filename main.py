import random

j = input("Enter the characters number of your password ")
j = int(j)


def aleatorio(max):
    return random.randint(0, max - 1)


def generarPassword(longitud):
    characters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ñ",
                  "z",
                  "x", "c", "v", "b", "n", "m", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "#", "$", "%",
                  "&",
                  "/", "=", "?", "¡", "¨", "*", ";", ":", "_"]
    password = ""
    for i in range(longitud):
        character = characters[aleatorio(len(characters))]
        password = password + character
    return password

print(generarPassword(j))
