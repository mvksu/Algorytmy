from timeit import default_timer as timer
import random
import sys

sys.setrecursionlimit(100000000)


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q)
        quickSort(A, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r+1):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    if i < r:
        return i
    else:
        return i-1

def quickSortBubble(A, p, r, c):
    if p < r:
        q = partition(A, p, r)
        if len(A[p:q+1]) < c:
            bubbleSort(A[p:q+1])
        if len(A[q+1:r+1]) < c:
            bubbleSort(A[q+1:r+1])
        quickSortBubble(A, p, q, c)
        quickSortBubble(A, q+1, r, c)

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

array1000 = [x for x in range(1000)]
arrayrandom1000 = [random.randint(0,1000) for x in range(1000)]

array5000 = [x for x in range(5000)]
arrayrandom5000 = [random.randint(0,5000) for x in range(5000)]

array10000 = [x for x in range(10000)]
arrayrandom10000 = [random.randint(0,10000) for x in range(15000)]

array15000 = [x for x in range(15000)]
arrayrandom15000 = [random.randint(0,15000) for x in range(15000)]

start1 = timer()
quickSort(array1000, 0, 999)
stop1 = timer()
czas1 = stop1 - start1

start2 = timer()
quickSort(arrayrandom1000, 0, 999)
stop2 = timer()
czas2 = stop2 - start2

start3 = timer()
quickSort(array5000, 0, 4999)
stop3 = timer()
czas3 = stop3 - start3

start4 = timer()
quickSort(arrayrandom5000, 0, 4999)
stop4 = timer()
czas4 = stop4 - start4

start5 = timer()
quickSort(array10000, 0, 9999)
stop5 = timer()
czas5 = stop5 - start5

start6 = timer()
quickSort(arrayrandom10000, 0, 9999)
stop6 = timer()
czas6 = stop6 - start6

start7 = timer()
quickSort(array15000, 0, 14999)
stop7 = timer()
czas7 = stop7 - start7

start8 = timer()
quickSort(arrayrandom15000, 0, 14999)
stop8 = timer()
czas8 = stop8 - start8

print("##################################################################")
print("Sortowanie quicksort")
print("##################################################################")
print("|--rozmiar tablicy-|-czas dane losowe---|-czas dane niekorzystne--|")
print("|--1000------------|"+str(czas2)+" | "+str(czas1)+" |")
print("|--5000------------|"+str(czas4)+" | "+str(czas3)+" |")
print("|--10000-----------|"+str(czas6)+" | "+str(czas5)+" |")
print("|--15000-----------|"+str(czas8)+" | "+str(czas7)+" |")

start1b = timer()
quickSortBubble(array1000, 0, 999)
stop1b = timer()
czas1b = stop1b - start1b

start2b = timer()
quickSortBubble(arrayrandom1000, 0, 999)
stop2b = timer()
czas2b = stop2b - start2b

start3b = timer()
quickSortBubble(array5000, 0, 4999)
stop3b = timer()
czas3b = stop3b - start3b

start4b = timer()
quickSortBubble(arrayrandom5000, 0, 4999)
stop4b = timer()
czas4b = stop4b - start4b

start5b = timer()
quickSortBubble(array10000, 0, 9999)
stop5b = timer()
czas5b = stop5b - start5b

start6b = timer()
quickSortBubble(arrayrandom10000, 0, 9999)
stop6b = timer()
czas6b = stop6b - start6b

start7b = timer()
quickSortBubble(array15000, 0, 14999)
stop7b = timer()
czas7b = stop7b - start7b

start8b = timer()
quickSortBubble(arrayrandom15000, 0, 14999)
stop8b = timer()
czas8b = stop8b - start8b

print("##################################################################")
print("Sortowanie z wykorzysztaniem bubblesort")
print("##################################################################")
print("|--rozmiar tablicy-|-czas dane losowe---|-czas dane niekorzystne--|")
print("|--1000------------|"+str(czas2)+" | "+str(czas1)+" |")
print("|--5000------------|"+str(czas4)+" | "+str(czas3)+" |")
print("|--10000-----------|"+str(czas6)+" | "+str(czas5)+" |")
print("|--15000-----------|"+str(czas8)+" | "+str(czas7)+" |")




