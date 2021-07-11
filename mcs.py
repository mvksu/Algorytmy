


def lcsLength(x,y):
    m = len(x)
    n = len(y)
    c = [[0 for i in range(n + 1)] for j in range(m + 1)]
    b = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:  # x[i-1] == y[j-1] przy
                c[i][j] = c[i-1][j-1] + 1  # indeksowaniu x,y od 0
                b[i][j] = "\\"
            else:
                if c[i-1][j] >= c[i][j - 1]:
                    c[i][j] = c[i-1][j]
                    b[i][j] = "|"
                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = "-"
    return c, b

def PrintLCS(x, b, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == "\\":
        PrintLCS(x, b, i - 1, j - 1)
        print(x[i-1])
    elif b[i][j] == "|":
        PrintLCS(x, b, i - 1, j)
    else:
        PrintLCS(x, b, i, j - 1)

x = "bacbacba"
y = "abbaac"
(a, b) = lcsLength(x, y)

for i in range(len(x)+1):
    for j in range(len(y)+1):
        print(f'{b[i][j]}{a[i][j]} ', end="")
    if i > 0:
        print(x[i-1])
    else:
        print("")
for j in range(len(y)):
    if j < 1:
        print("    ", end="")
    print(f"{y[j]}  ", end="")

print("")
PrintLCS(x, b, 8, 6)

