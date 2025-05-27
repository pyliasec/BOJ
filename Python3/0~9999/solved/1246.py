def a(b, c, d):
    d.sort()
    
    e = 0
    f = 0

    for i in range(c):
        g = d[i]
        h = 0
        for x in d:
            if x >= g:
                h += 1
            if h == b:
                break
        i = g * min(h, b)
        if i > e:
            e = i
            f = g
    
    return f, e

b, c = map(int, input().strip().split())
d = [int(input().strip()) for _ in range(c)]

result = a(b, c, d)
print(result[0], result[1])