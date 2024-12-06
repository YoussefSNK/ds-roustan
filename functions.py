


def several_zeros():
    print("0" * 10)


def several_zeros_custom(nb_zeros):
    print("0" * nb_zeros)




# à check plus tard
def matrix(rows, cols):
    liste = []
    listea = []
    for i in range(cols):
        liste.append(0)
    
    print(liste)

    for i in range(rows):
        listea.append(liste)
    print(listea)



if __name__ == '__main__':
    several_zeros()
    several_zeros_custom(10)

    matrix(3,2)
    matrix(10,5)