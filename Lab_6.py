def generare_cnp(sex, an, luna, zi, judet, nr):
    cnp = ''
    if sex == 'M':
        if an < 2000:
            cnp += '1'
            if an - 1900 < 10:
                cnp += '0'
            cnp += str(an-1900)
        else:
            cnp += '5'
            if an - 2000 < 10:
                cnp += '0'
            cnp += str(an-2000)
    elif sex == 'F':
        if an < 2000:
            cnp += '2'
            if an - 1900 < 10:
                cnp += '0'
            cnp += str(an-1900)
        else:
            cnp += '6'
            if an - 1900 < 10:
                cnp += '0'
            cnp += str(an-2000)
    if luna < 10:
        cnp += '0'
    cnp += str(luna)
    if zi < 10:
        cnp += '0'
    cnp += str(zi)
    if judet < 10:
        cnp += '0'
    cnp += str(judet)
    if nr < 10:
        cnp += '00'
    elif nr < 100:
        cnp += '0'
    cnp += str(nr)
    cnp += str(generarec(cnp))
    return cnp


def generarec(sir):
    numar_generare = '279146358279'
    cifra_control = 0
    for i in range(len(sir)):
        cifra_control += int(sir[i]) * int(numar_generare[i])
    cifra_control %= 11
    if cifra_control == 10:
        cifra_control = 1
    return cifra_control


def cautare_simpla(lista, x):
    for i in range(len(lista)):
        if lista[i] == x:
            return i
    return -1


if __name__ == '__main__':
    print(cautare_simpla([1, 4, 6, 8, 10, 10], 10))
    print(generare_cnp('M', 2003, 7, 1, 24, 504))
