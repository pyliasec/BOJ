import sys

def a(b, c, d):
    e = [i for i in range(c + 1)]
    d.sort()

    for i in range(c + 1):
        if i > 0:
            e[i] = min(e[i], e[i-1] + 1)
            
        while d and d[0][0] == i:
            f, g, h = d.pop(0)
            if g <= c:
                e[g] = min(e[g], e[f] + h)

    return e[c]

b, c = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(b)]

print(a(b, c, d))