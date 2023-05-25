def fisiere():
    file = open("Fisier.txt", 'r+')
    vect_cuvinte = file.read()
    vect_cuvinte = vect_cuvinte.split()
    i = 0
    print(vect_cuvinte)
    while i < len(vect_cuvinte)-1:
        if int(vect_cuvinte[i])+1 != int(vect_cuvinte[i+1]):
            vect_cuvinte.insert(i+1, str(int(vect_cuvinte[i])+1))
            file.write(str(int(vect_cuvinte[i])+1))
            file.write('\n')
        i = i + 1
    print(vect_cuvinte)
    line = file.readline()
    while line != '':
        print(line)
        print(file.tell())
        line = file.readline()

    # f5 = 0
    # for i in range(len(vect_cuvinte)):
    #     if vect_cuvinte[i].startswith('5'):
    #         f5 = 1

    file.close()


if __name__ == '__main__':
    fisiere()
