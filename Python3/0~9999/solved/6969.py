from collections import deque

def b(n, t):
    s = (0, 0)
    e = (n-1, n-1)
    v = [[float('inf')] * n for _ in range(n)]
    v[0][0] = 0
    q = deque([(0, s)])
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        o, (x, y) = q.popleft()
        if (x, y) == e:
            return o
        for i, j in d:
            a, c = x + i, y + j
            if 0 <= a < n and 0 <= c < n:
                if abs(t[a][c] - t[x][y]) <= 2:
                    p = o + (1 if t[a][c] > t[0][0] or t[x][y] > t[0][0] else 0)
                    if p < v[a][c]:
                        v[a][c] = p
                        if p > o:
                            q.append((p, (a, c)))
                        else:
                            q.appendleft((p, (a, c)))
    return "CANNOT MAKE THE TRIP"

r = int(input())
for i in range(r):
    n = int(input())
    t = []
    for _ in range(n):
        w = [int(input()) for _ in range(n)]
        t.append(w)
    u = b(n, t)
    if isinstance(u, int):
        print(u)
    else:
        print(u)
    
    if i < r - 1:
        print()