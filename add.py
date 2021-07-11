def quickSortBubble(A, p, r, c):
    if p < r:
        q = partition(A, p, r)
        if len(A[p:q+1]) < c:
            bubbleSort(A[p:q+1])
        quickSortBubble(A, q + 1, r, c)
        if len(A[q+1:r+1]) < c:
            bubbleSort(A[q+1:r+1])
        quickSortBubble(A, p, q, c)
        

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

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


A = [5, 4, 1, 0, 2, 9, 11, 33, 22, 10]
quickSortBubble(A, 0, 9, 4)
print(A)

