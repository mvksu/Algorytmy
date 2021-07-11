# A = [ 73, 83, 13, 7, 49, 15, 71 , 93, 42, 29 ]

A = [ 98, 64, 68, 63, 27, 43, 67, 46, 28, 14 ]

def heapifyIterative(A, heapSize, i):
    while True:
        l = 2 * i + 1
        r = 2 * i + 2
        if l < heapSize and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < heapSize and A[r] > A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            i = largest
        else:
            break
    return A

def buildHeapIterative(A):
    heapSize = len(A)
    k = int((len(A)-2)/2)
    for i in range(k, -1, -1):
        heapifyIterative(A, heapSize, i)
    return A

# buildHeapIterative(A)
# print("Kopcowanie iteratywnie")
# print(A)

def heapifyRecurisve(A, heapSize, i):
    l = 2*i+1 # lewy syn
    r = 2*i+2 # prawy syn
    if l < heapSize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heapSize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapifyRecurisve(A, heapSize, largest)
    return A

def buildHeapRecursive(A):
    heapSize = len(A)
    k = int((len(A)-2)/2) # ojciec ostatniego
    # węzła
    for i in range(k, -1, -1):
        heapifyRecurisve(A, heapSize, i)
    return A

# print("Kopcowanie rekursywnie")
# buildHeapRecursive(A)
# print(A)
#
# plik = open("f1.txt", "r")
# A = plik.readlines()
# plik.close()
# def heapSort(A):
#     A = buildHeapRecursive(A)
#     heapSize = len(A)
#     for i in range(len(A)-1, 0, -1):
#         A[0], A[heapSize-1] = A[heapSize-1], A[0]
#         heapSize -= 1
#         heapifyRecurisve(A,heapSize,0)
#     return A
#
# plik = open("f1.txt", "a")
# plik.writelines(heapSort(A))

# print(A)
#
def heapSort(A):
    A = buildHeapRecursive(A)
    heapSize = len(A)
    for i in range(len(A)-1, len(A)-4, -1):
        A[0], A[heapSize-1] = A[heapSize-1], A[0]
        heapSize -= 1
        heapifyRecurisve(A,heapSize,0)
    return A
heapSort(A)

print(A)



