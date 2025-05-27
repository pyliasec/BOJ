from collections import deque
import sys

def a(b, c, d):
    d[c] = True
    print(c, end=' ')
    for e in sorted(b[c]):
        if not d[e]:
            a(b, e, d)

def f(b, g, d):
    h = deque([g])
    d[g] = True
    while h:
        c = h.popleft()
        print(c, end=' ')
        for e in sorted(b[c]):
            if not d[e]:
                h.append(e)
                d[e] = True

n, m, v = map(int, sys.stdin.readline().split())
b = [[] for _ in range(n+1)]

for _ in range(m):
    j, k = map(int, sys.stdin.readline().split())
    b[j].append(k)
    b[k].append(j)

d = [False] * (n+1)
a(b, v, d)
print()

d = [False] * (n+1)
f(b, v, d)