def decrypt(message : [int]) -> str:
    liste = []
    for i in range (len(message)):
        liste.append(chr(message[i]))
    return ''.join(liste)


if __name__ == '__main__':
    pass