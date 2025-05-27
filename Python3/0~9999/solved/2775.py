def a(k, n):
    b = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, n + 1):
        b[0][i] = i
    
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            b[i][j] = b[i][j - 1] + b[i - 1][j]

    return b[k][n]

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(a(k, n))