def min_max(n):
    max = -1
    maxi = []
    min = 1000000
    mini = []
    mat = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = int(input())
            if mat[i][j] > max:
                max = mat[i][j]
                maxi = [i, j]
            if mat[i][j] < min:
                min = mat[i][j]
                mini = [i, j]
    print("Minimul", min, "pe pozitia", mini, "si maximul", max, "pe pozitia", maxi)


def prob_2(matrice):
    # mat patratica sa se genereze elem matricii dupa urm. regul: pentru care produsului indicilor este un nr par vor
    # avea val 1 elem pt care prod indicilor nr impar vor avea val 0 si de pe diag principala 2
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if i == j:
                matrice[i][j] = 2
            elif i*j % 2 == 0:
                matrice[i][j] = 1
            else:
                matrice[i][j] = 0
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            print(matrice[i][j], end=" ")
        print()


def unire(st, dr):
    i = 0
    j = 0
    lista_sortata = []
    while i < len(st) and j < len(dr):
        if st[i] < dr[j]:
            lista_sortata.append(st[i])
            i += 1
        else:
            lista_sortata.append(dr[j])
            j += 1
    while i < len(st):
        lista_sortata.append(st[i])
        i += 1
    while j < len(dr):
        lista_sortata.append(dr[j])
        j += 1
    return lista_sortata


def msort(lista):
    if len(lista) <= 1:
        return lista
    else:
        mij = len(lista) // 2
        stanga = msort(lista[:mij])
        dreapta = msort(lista[mij:])
        return unire(stanga, dreapta)


if __name__ == '__main__':
    min_max(n)
    mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    prob_2(mat)
    lista_de_sortat = [10, 5, 2, 25, 3, 1, 8]
    print(msort(lista_de_sortat))
