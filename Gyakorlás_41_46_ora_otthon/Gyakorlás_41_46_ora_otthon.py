# 1.
def gyakorlas():
    f = open("c:/Users/Dell/Documents/SZOFTVERFEJLESZTŐ/Programozás/adatsorok.txt", 'r')
    diakok = f.read().split('\n')
    f.close
    print(diakok)
    print()

    eredmenyek = []
    for i in range(0,len(diakok)):
        sor = diakok[i].split(' ')
        osszeg = 0
        for j in range(1,len(sor)):
            osszeg += int(sor[j])
        eredmenyek.append(osszeg)
    print(eredmenyek)
    print()

    maxi = 0
    for k in range(0,len(eredmenyek)):
        if (eredmenyek[k] > eredmenyek[maxi]):
            maxi = k
    print(maxi+1)
    seged = diakok[maxi].split(' ')
    print("A legeredményesebb diák: ", seged[0])
    print()


gyakorlas()