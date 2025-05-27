import heapq
import sys

def f(n, m, k, r):
    g = [[] for _ in range(n + 1)]
    for a, b, c in r:
        g[a].append((b, c))

    d = [[] for _ in range(n + 1)]
    q = [(0, 1)]

    while q:
        t, c = heapq.heappop(q)

        if len(d[c]) == k:
            continue

        heapq.heappush(d[c], -t)

        if len(d[c]) == k:
            t = -d[c][0]

        for x, y in g[c]:
            z = t + y
            if len(d[x]) < k or z < -d[x][0]:
                heapq.heappush(q, (z, x))

    s = []
    for i in range(1, n + 1):
        s.append(-1 if len(d[i]) < k else -d[i][0])

    return s

input = sys.stdin.readline
n, m, k = map(int, input().split())
r = [tuple(map(int, input().split())) for _ in range(m)]

result = f(n, m, k, r)
print(*result, sep='\n')