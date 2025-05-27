def f(n, b, a, p):
    p.sort()
    c = 0
    r = -1
    for i in range(min(a, n)):
        d = p[i] // 2
        if c + d <= b:
            c += d
        else:
            r = i
            break
    if r == -1:
        r = a
        s = 0
        for i in range(a, n):
            x = p[s] // 2
            y = p[i] // 2
            if c + x + y <= b:
                c += (x + y)
                r += 1
                s += 1
            else:
                break
    return r

n, b, a = map(int, input().split())
p = list(map(int, input().split()))
print(f(n, b, a, p))