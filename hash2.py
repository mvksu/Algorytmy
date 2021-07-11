m = 389
file = open("nazwiska.txt", "r")
tab = [ [] for x in range(m)]

def funkcja(k):
    result = 0
    for c in k:
        result = (result + ord(c)) * 111
    return result



def Wstaw(k, i):
    p=1
    while True:
        hk = (funkcja(k[1]) + i) % m
        if not tab[hk]:
            tab[hk].append(k)
            #print(tab)
            #print("próba: " + str(i + 1) )
            return p
        p = p + 1
        #i = i + 1           # liniowe
        #i = i + 1 + i ** 2  # kwadratowe
        i = i * (1 + (funkcja(k[1]) % (m-2)))#dwukrotne


def main(procent):
    i = 0
    proby = 0
    while i <= m:
        i = i + 1
        if i / len(tab) <= procent:
            k = file.readline().strip('\n').split(" ")
            proby = proby + Wstaw(k, 0)
        else:
            print("Tablica zapełniona do " + str(procent * 100) + "%")
            print("Średnia ilość prób: " + str(proby / i))
            break

main(0.5)


# m = 10079
# Tablica zapełniona do 50.0%
# Średnia ilość prób: 1.4726190476190477
# Tablica zapełniona do 70.0%
# Średnia ilość prób: 2.0904195011337867
# Tablica zapełniona do 90.0%
# Średnia ilość prób: 4.635471781305115
