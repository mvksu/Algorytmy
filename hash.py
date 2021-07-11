
file = open("3700.txt", "r")

def W(k):
    return hash(k)

def D(k):
    result = 0
    for c in k:
        result = (result + ord(c))*111
    return result

def S(k):
    result = 0
    for c in k:
        result = result + ord(c)
    return result

def count(tab):
    count = 0
    for i in tab:
        if not i:
            count = count + 1
    print('ilosc pustych: ' + str(count))

def max(tab):
    lenmax = 0
    for i in tab:
        if len(i) > lenmax:
            lenmax = len(i)
    print('najdłuższa lista w tablicy: ' + str(lenmax))

def avg(tab):
    all = 0
    counts = 0
    for i in tab:
        if i:
            all = all + len(i)
            counts = counts + 1
    avg = all / counts
    print('średnia długość to: ' + str(avg))


m = 17
tab1 = [ [] for x in range(m)]
tab2 = [ [] for x in range(m)]
tab3 = [ [] for x in range(m)]


for i in range(m):
    k = file.readline().strip()
    hk = W(k) % m
    tab1[hk].append(k)
print("W17:")
# print(tab1)
count(tab1)
max(tab1)
avg(tab1)

for i in range(m):
    k = file.readline().strip()
    hk = D(k) % m
    tab2[hk].append(k)
print("D17:")
# print(tab2)
count(tab2)
max(tab2)
avg(tab2)

for i in range(m):
    k = file.readline().strip()
    hk = S(k) % m
    tab3[hk].append(k)
print("S17:")
# print(tab3)
count(tab3)
max(tab3)
avg(tab3)

print("")
m = 1031
tab1 = [ [] for x in range(m)]
tab2 = [ [] for x in range(m)]
tab3 = [ [] for x in range(m)]


for i in range(m):
    k = file.readline().strip()
    hk = W(k) % m
    tab1[hk].append(k)
print("W1031:")
# print(tab1)
count(tab1)
max(tab1)
avg(tab1)

for i in range(m):
    k = file.readline().strip()
    hk = D(k) % m
    tab2[hk].append(k)
print("D1031:")
# print(tab2)
count(tab2)
max(tab2)
avg(tab2)

for i in range(m):
    k = file.readline().strip()
    hk = S(k) % m
    tab3[hk].append(k)
print("S1031:")
# print(tab3)
count(tab3)
max(tab3)
avg(tab3)

print("")
file = open("3700.txt", "r")
m = 1024
tab1 = [ [] for x in range(m)]
tab2 = [ [] for x in range(m)]
tab3 = [ [] for x in range(m)]


for i in range(m):
    k = file.readline().strip()
    hk = W(k) % m
    tab1[hk].append(k)
print("W1024:")
# print(tab1)
count(tab1)
max(tab1)
avg(tab1)

for i in range(m):
    k = file.readline().strip()
    hk = D(k) % m
    tab2[hk].append(k)
print("D1024:")
# print(tab2)
count(tab2)
max(tab2)
avg(tab2)

for i in range(m):
    k = file.readline().strip()
    hk = S(k) % m
    tab3[hk].append(k)
print("S1024:")
# print(tab3)
count(tab3)
max(tab3)
avg(tab3)


# 1031 i 1024 dawały podobne wyniki
# tak




