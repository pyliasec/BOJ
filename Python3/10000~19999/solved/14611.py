from heapq import *

I = float('inf')
n, m = map(int, input().split())
v = [[I]*m for _ in range(n)]
for i in range(n):
    r = list(map(int, input().split()))
    for j in range(m):
        if r[j] == -2: v[i][j] = 0
        elif r[j] >= 0: v[i][j] = r[j]

d = [[I]*m for _ in range(n)]
q = []
for i in range(m):
    if v[0][i] < I:
        heappush(q, (v[0][i], 0, i))
        d[0][i] = v[0][i]
for i in range(n):
    if v[i][m-1] < I:
        heappush(q, (v[i][m-1], i, m-1))
        d[i][m-1] = v[i][m-1]

while q:
    c, y, x = heappop(q)
    if d[y][x] < c: continue
    for dy, dx in [(-1,-1), (-1,0), (-1,1), (1,-1), (1,0), (1,1), (0,-1), (0,1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and v[ny][nx] < I:
            nc = c + v[ny][nx]
            if d[ny][nx] > nc:
                d[ny][nx] = nc
                heappush(q, (nc, ny, nx))

a = min(min(d[i][0] for i in range(n)), min(d[n-1]))
print(a if a < I else -1)