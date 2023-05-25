def cautare(lista, nr):
    ok = 0
    for i in range(len(lista)):
        if lista[i] == nr:
            print("DA")
            ok = 1
    if ok == 0:
        print("NU")


def bubble(l):
    switch = True
    while switch:
        switch = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                switch = True
    return l


def mergesort(l):
    n = len(l)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if l[j] < l[min]:
                min = j
        if min != i:
            aux = l[i]
            l[i] = l[min]
            l[min] = aux
    return l


employee1 = {
        'id': 14,
        'name': 'Andrei',
        'age': 20,
        'position': 'Manager.'
}
employee2 = {
        'id': 120,
        'name': 'Darius',
        'age': 18,
        'position': 'Developer.'
}
employee3 = {
        'id': 25,
        'name': 'Alex',
        'age': 25,
        'position': 'Tester.'
}
employee4 = {
        'id': 2,
        'name': 'George',
        'age': 22,
        'position': 'Leader.'
}


def cautareangajat(list1):
    for i in range(len(list1)):
        last = list(list1[i].values())[0]
        if last == 2:
            print(list1[i])


if __name__ == '__main__':
    lista = [1, 5, 2, 10]
    cautare(lista, 10)
    bubble(lista)
    mergesort(lista)
    cautareangajat(lista)
