def several_zeros():
    return [0] * 10


def several_zeros_custom(nb_zeros):
    return [0] * nb_zeros


# ça marche je crois
def matrix(rows, cols):
    liste = []
    listea = []
    for i in range(cols):
        liste.append(0)
    for i in range(rows):
        listea.append(liste)

# demander plus tard pour le bail de la liste
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.ligne = []
        self.matrice = []
        for i in range(cols):
            self.ligne.append(0)
        for i in range(rows):
            self.matrice.append(self.ligne)
        print(self.matrice)


    def get_value(self, row, col):
        return self.matrice[col][row]

    def __eq__(self, deux):
        return self.matrice == deux.matrice




if __name__ == '__main__':
    print(several_zeros())
    # several_zeros_custom(10)

    matrix(3,2)
    matrix(10,5)

    a = Matrix(3,2)
    b = Matrix(3,3)
    print(a==b)