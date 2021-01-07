# 1.
def gyakorlas():
    f = open("c:/Users/Dell/Documents/SZOFTVERFEJLESZTŐ/Programozás/adatsorok.txt", 'r')
    diakok = f.read().split('\n')
    print(diakok)
    f.close()
    print()

    lista = []
    for i in range(0,len(diakok)):
        sor = diakok[i].split(' ')
        osszeg = 0
        for j in range(1,len(sor)):
            osszeg += int(sor[j])
        lista.append(osszeg)
    print(lista)
    print()

    maxi = 0
    for k in range(0,len(lista)):
        if(lista[k]>lista[maxi]):
            maxi = k
    print(maxi+1)
    sv = diakok[maxi].split(' ')
    print("A legjobb versenyző: ",sv[0])
    print()


gyakorlas()