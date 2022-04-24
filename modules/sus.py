import math


def read_file(x):
    wynik = []

    f = open(x, "r")
    for a in f:
        # print(a)
        # print(a.split(","))
        linia = []
        for b in a.rstrip("\n").split(","):
            linia.append(b)
        wynik.append(linia)
    f.close()
    return wynik


def stworz_slownik(d, c):
    Dict = {}
    for k in d:
        if k[c] not in Dict:
            Dict[k[c]] = 1
        else:
            Dict[k[c]] += 1
        # print(k)
    return Dict


def entropia(data, k=-1):
    Slownik = stworz_slownik(data, k)
    # print(Slownik)
    l = len(data)
    wynik = 0
    for a in Slownik.values():
        x = a / l
        wynik += x * math.log(x, 2)
    return -1 * round(wynik, 2)
    # print(Slownik.values())


def informacja(x, t):
    Slownik = stworz_slownik(t, x)
    wynik = 0
    for a in Slownik:
        temp = [b for b in t if b[x] == a]
        # print(temp)
        en = entropia(temp)
        # print(en)
        wynik += Slownik[a] / len(t) * en
    return wynik


def gain(x, t):
    return entropia(t) - informacja(x, t)


def gain_ratio(x, t):
    # print(entropia(t, x))
    # print(f'entropia{entropia(t,x)}')
    if entropia(t, x) == 0:
        return 0
    return gain(x, t) / entropia(t, x)


def dane_wyjsciowe(d):
    #print(m(d))
    for n in range(len(d[0]) - 1):
        print(f'\nInfo(' + str(n) + ')= ' + str(informacja(n, d)) + '\nGain= ' + str(gain(n, d)))
        print(f'Gainratio=' + str(gain_ratio(n, d)))


def m(d):
    # i,w
    i, w = 0, gain_ratio(0, d)

    for n in range(1, len(d[0]) - 1):
        t = gain_ratio(n, d)
        if t > w:
            i, w = n, t
    #print(i,w)
    return i, w
    # print(f'Gainratio=' + str(gain_ratio(n, d)))


def drzewo(d, n=0):
    # print(d)
    space = '    ' * n
    i, w = m(d)
    if w == 0:
        print(f'{space}lisc - decyzja {d[0][-1]}')
        return None
    print(f'{space}podział wg atrybutu a{i+1}')

    Slownik = stworz_slownik(d, i)
    values = list(Slownik.keys())
    for a in range(len(Slownik)):
        temp = []
        for numer,b in enumerate(d):
            # print(b)
            if b[i] == values[a]:
                temp.append(b)
                #temp.append(b[:i] +[numer]+ b[i + 1:])
        print(f'{space}value - {values[a]}')
        #print(temp)
        drzewo(temp, n + 1)
        # print(temp)
    # print(dane)



#d - ścieżka do danych
#dane = read_file(d)

#dane_wyjsciowe(dane)
#drzewo(dane)

