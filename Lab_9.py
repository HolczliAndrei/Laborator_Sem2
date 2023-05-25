def cautare_graf(graf, start, noduri_parcurse):
    curentn = start
    for nod in graf:
        if nod[0] == curentn:
            noduri_parcurse.append(nod[0])
            curentn = nod[1]
    noduri_parcurse.append(curentn)


def backtracking(lista):
    solutii = []
    partial = []
    backtrack(lista, partial, solutii)
    return solutii


def backtrack(lista, partial, solutii):
    if is_solution(lista, partial):
        solutii.append(partial.copy())
        return
    for element in lista:
        if element not in partial:
            partial.append(element)
            backtrack(lista, partial, solutii)
            partial.pop()


def is_solution(lista, partial):
    return len(partial) == len(lista)


if __name__ == '__main__':
    graf = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4], [2, 6], [4, 5], [5, 7]]
    noduri_parcurse = []
    cautare_graf(graf, 0, noduri_parcurse)
    print(noduri_parcurse)
    lista_exemplu = [1, 2, 3]
    rezultat = backtracking(lista_exemplu)
    print(rezultat)
