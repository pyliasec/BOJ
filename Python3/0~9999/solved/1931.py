def f(n, m):
    m.sort(key=lambda x: (x[1], x[0]))
    
    a = 0
    b = 0
    
    for x, y in m:
        if x >= b:
            a += 1
            b = y
    
    return a












n = int(input())
m = [tuple(map(int, input().split())) for _ in range(n)]

c = f(n, m)
print(c)
