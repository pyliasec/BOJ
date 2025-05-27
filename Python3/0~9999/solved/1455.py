def f(N, M, c):
    fc = 0
    
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if c[i][j] == '1':
                fc += 1
                for x in range(i+1):
                    for y in range(j+1):
                        c[x][y] = '1' if c[x][y] == '0' else '0'
    
    return fc

N, M = map(int, input().split())
c = [list(input().strip()) for _ in range(N)]

result = f(N, M, c)
print(result)