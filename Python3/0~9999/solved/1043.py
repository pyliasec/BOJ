def f(x):
    if p[x] != x:
        p[x] = f(p[x])
    return p[x]

def u(a, b):
    a = f(a)
    b = f(b)
    if a != b:
        p[b] = a

n, m = map(int, input().split())
a = list(map(int, input().split()))
t = a[0]
l = a[1:] if t else []
p = [i for i in range(n + 1)]
P = []
for _ in range(m):
    a = list(map(int, input().split()))
    k = a[0]
    L = a[1:]
    P.append(L)
    for i in range(1, len(L)):
        u(L[0], L[i])
S = set()
for x in l:
    S.add(f(x))
c = 0
for L in P:
    f1 = True
    for x in L:
        if f(x) in S:
            f1 = False
            break
    if f1:
        c += 1
print(c)