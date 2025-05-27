def c(a, b):
    if a == 0:
        return float('inf')
    d = 0
    while a % b == 0:
        a //= b
        d += 1
    return d

def z(n, m):
    p = [[0] * n for _ in range(n)]
    q = [[0] * n for _ in range(n)]
    
    p[0][0] = c(m[0][0], 2)
    q[0][0] = c(m[0][0], 5)
    
    for j in range(1, n):
        if m[0][j] == 0:
            p[0][j] = q[0][j] = float('inf')
        else:
            p[0][j] = p[0][j-1] + c(m[0][j], 2)
            q[0][j] = q[0][j-1] + c(m[0][j], 5)
    
    for i in range(1, n):
        if m[i][0] == 0:
            p[i][0] = q[i][0] = float('inf')
        else:
            p[i][0] = p[i-1][0] + c(m[i][0], 2)
            q[i][0] = q[i-1][0] + c(m[i][0], 5)
    
    for i in range(1, n):
        for j in range(1, n):
            if m[i][j] == 0:
                p[i][j] = q[i][j] = float('inf')
            else:
                r = c(m[i][j], 2)
                s = c(m[i][j], 5)
                p[i][j] = min(p[i-1][j], p[i][j-1]) + r
                q[i][j] = min(q[i-1][j], q[i][j-1]) + s
    
    return min(p[n-1][n-1], q[n-1][n-1])

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
result = z(n, m)
print(result)