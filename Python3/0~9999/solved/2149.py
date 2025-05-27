def d(k, c):
    l = len(k)
    n = len(c) // l

    s = sorted((char, i) for i, char in enumerate(k))
    
    m = [[''] * l for _ in range(n)]
    
    index = 0
    for char, o in s:
        for row in range(n):
            m[row][o] = c[index]
            index += 1

    p = ''.join(m[row][col] for row in range(n) for col in range(l))
    
    return p

k = input().strip()
c = input().strip()

print(d(k, c))