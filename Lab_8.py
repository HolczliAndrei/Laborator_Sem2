import random


def zaruri():
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)
    if zar1 == zar2:
        return True
    else:
        return False


def zaruri_1000():
    castiguri = 0
    for i in range(1000):
        rez = zaruri()
        if rez:
            castiguri += 1
    print("Sansa de castig este de", castiguri*100/1000, "%")


def dimensiune_mat(lista):
    max = 0
    for punct in lista:
        for coord in punct:
            if coord > max:
                max = coord
    return max


def generare_mat(lista):
    dim = dimensiune_mat(lista)+1
    matrice_adiacenta = [[0] * dim for i in range(dim)]
    for punct in lista:
        matrice_adiacenta[punct[0]][punct[1]] = 1
        matrice_adiacenta[punct[1]][punct[0]] = 1
    return matrice_adiacenta


def generare_lista(mat):
    lista = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if j > i and mat[i][j] == 1:
                lista.append([i, j])
    print(lista)


if __name__ == '__main__':
    lista_adiacenta = [[0, 1], [0, 2], [1, 2], [1, 3], [3, 4]]
    matrice = generare_mat(lista_adiacenta)
    zaruri_1000()
    generare_lista(matrice)
