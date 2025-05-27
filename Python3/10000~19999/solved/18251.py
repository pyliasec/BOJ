import math

n = int(input())
w = [0] + [int(x) for x in input().split()]

class p:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

c = 1
q = []

def t(x, y):
    global c
    if x*2 <= n:
        t(x*2, y-1)
    q.append(p(c, y, w[x]))
    c += 1
    if x*2+1 <= n:
        t(x*2+1, y-1)

def l(a):
    r = 0
    while a:
        a //= 2
        r += 1
    return r

h = l(n)
s = 0
m = -9999999999
for i in range(1, n+1):
    s += w[i]
    m = max(m, w[i])

if m < 0:
    print(m)
    exit()

t(1, h)

a = 0
for y1 in range(1, h+1):
    for y2 in range(y1, h+1):
        x = 0
        for i in range(n):
            if q[i].y < y1 or y2 < q[i].y:
                continue
            x = max(x + q[i].z, 0)
            a = max(a, x)

print(a)