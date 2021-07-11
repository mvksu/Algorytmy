import math
from timeit import default_timer as timer

import sys

def f1(n):
    s = 0
    for j in range(1, n):
        s = s + 1 / j
    return s


def f2(n):
    s = 0
    for j in range(1, n):
        for k in range(1, n):
            s = s + k / j
    return s


def f3(n):
    s = 0
    for j in range(1, n):
        for k in range(j, n):
            s = s + k / j
    return s


def f4(n):
    s = 0
    for j in range(1, n):
        k = 2
        while k <= n:
            s = s + k / j
            k = k * 2
    return s


def f5(n):
    s = 0
    k = 2
    while k <= n:
        s = s + 1 / k
        k = k * 2
    return s


nn = [2000, 4000, 8000, 16000, 32000]
# with open("f1.txt", "w") as f1file:
#     for n in nn:
#         start = timer()
#         f1(n)
#         stop = timer()
#         Tn = stop - start
#         Fn = n
#         print(n, Tn, Fn / Tn, file=f1file)
# f1file.close()
# with open("f2.txt", "w") as f2file:
#     for n in nn:
#         start = timer()
#         f2(n)
#         stop = timer()
#         Tn = stop - start
#         Fn = n*n
#         print(n, Tn, Fn / Tn, file=f2file)
# f2file.close()
# with open("f3.txt", "w") as f3file:
#     for n in nn:
#         start = timer()
#         f3(n)
#         stop = timer()
#         Tn = stop - start
#         Fn = 100*n
#         print(n, Tn, Fn / Tn, file=f3file)
# f3file.close()
# with open("f4.txt", "w") as f4file:
#     for n in nn:
#         start = timer()
#         f4(n)
#         stop = timer()
#         Tn = stop - start
#         Fn = n*math.log(n,2)
#         print(n, Tn, Fn / Tn, file=f4file)
# f4file.close()
with open("f5.txt", "w") as f5file:
    for n in nn:
        start = timer()
        f5(n)
        stop = timer()
        Tn = stop - start
        Fn = math.log(n,2)
        print(n, Tn, Fn / Tn, file=f5file)
f5file.close()


# inne funkcje czasu:

# Fn=math.log(n,2)
# Fn=n
# Fn=100*n
# Fn=n*math.log(n,2)
# Fn=n*n