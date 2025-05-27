def a(N, b):
    b.sort(key=lambda x: (x[0], x[1]))
    
    c = [1] * N
    
    for i in range(1, N):
        for j in range(i):
            if b[i][0] > b[j][0] and b[i][1] > b[j][1]:
                c[i] = max(c[i], c[j] + 1)
    
    return max(c)

N = int(input())
b = [tuple(map(int, input().split())) for _ in range(N)]

print(a(N, b))
