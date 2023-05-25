def pb_rest(rest):
    lista_bancnote = [1, 2, 5, 10, 20, 50, 100]
    lista_rest = [0] * len(lista_bancnote)
    lista_bancnote = lista_bancnote[::-1]
    for i in range(len(lista_bancnote)):
        while lista_bancnote[i] <= rest:
            rest -= lista_bancnote[i]
            lista_rest[i] += 1
    return lista_rest[::-1]


def fibbonacci(n):
    if n == 1:
        return 0
    fib = [0] * n
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib


if __name__ == '__main__':
    print(pb_rest(226))
    print(fibbonacci(1))
