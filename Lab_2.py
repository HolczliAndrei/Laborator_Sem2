def masini(timp_lucru, timp_masini):
    timp_masini.sort()
    lista_masini_reparate = []
    for i in range(len(timp_masini)):
        if timp_masini[i] <= timp_lucru:
            lista_masini_reparate.append(timp_masini[i])
            timp_lucru -= timp_masini[i]
    return lista_masini_reparate


def masini_2(timp_lucru, timp_masini):
    timp_masini.sort()
    lista_masini_reparate = []
    i = 0
    while i < len(timp_masini) and timp_masini[i] <= timp_lucru:
        lista_masini_reparate.append(timp_masini[i])
        timp_lucru -= timp_masini[i]
        i += 1
    return lista_masini_reparate


def suma_recursiva(lista):
    if len(lista) == 1:
        if lista[0] % 2 == 0:
            return lista[0]
        else:
            return 0
    else:
        mijloc = len(lista) // 2
        return suma_recursiva(lista[:mijloc]) + suma_recursiva(lista[mijloc:])


def list_max(lista):
    ok = 0
    maxim = 0
    for i in range(len(lista)):
        if ok == 0:
            ok = 1
            maxim = lista[i]
        elif maxim < lista[i]:
            maxim = lista[i]
    return maxim


if __name__ == '__main__':
    print("Introdutei numarul de ore de lucru: ", end="")
    n = int(input())
    lista = [2, 5, 7, 20, 10]
    print("Aveti timp pentru", len(masini_2(n, lista)), "masini.")
    print(suma_recursiva([2, 5, 10, 20, 99]))
    print(list_max([10, 21, 50, 100]))
