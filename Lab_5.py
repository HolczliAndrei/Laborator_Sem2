def min_max(lista):
    minim = lista[0]
    maxim = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maxim:
            maxim = lista[i]
        if lista[i] < minim:
            minim = lista[i]
    return minim, maxim


def min2_max2(lista):
    # minim = lista[0]
    # minim2 = lista[0]
    # maxim = lista[0]
    # maxim2 = lista[0]
    lista.sort()
    minim = lista[0]
    minim2 = lista[1]
    maxim = lista[len(lista)-1]
    maxim2 = lista[len(lista)-2]
    # for i in range(1, len(lista)):
    #     if lista[i] > maxim:
    #         maxim2 = maxim
    #         maxim = lista[i]
    #     elif lista[i] > maxim2:
    #         maxim2 = lista[i]
    #     if lista[i] < minim:
    #         minim2 = minim
    #         minim = lista[i]
    #     elif lista[i] < minim2:
    #         minim2 = lista[i]
    print(minim * minim2, maxim * maxim2)


def parcurgere(mat):
    randuri = len(mat)
    coloane = len(mat[0])
    sir = "abc"
    for i in range(randuri):
        for j in range(coloane):
            if mat[i][j] == 1:
                print('(', sir[i], sir[j], end=" ) ")


def nr_cif_zero(n):
    if n == 0:
        return 0
    if n % 10 == 0:
        return 1 + nr_cif_zero(n//10)
    else:
        return 0 + nr_cif_zero(n//10)


if __name__ == '__main__':
    l = [21, 4, 64, 10, 2, 8, 100]
    mat = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
    print(min_max(l))
    min2_max2(l)
    parcurgere(mat)
    print(nr_cif_zero(10)) # numarul este mai mare ca 0
