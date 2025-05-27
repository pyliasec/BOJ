import heapq
import sys

def d(g, s, n):
    t = [float('inf')] * (n + 1)
    t[s] = 0
    q = [(0, s)]

    while q:
        c, v = heapq.heappop(q)

        if t[v] < c:
            continue

        for a, w in g[v]:
            r = c + w
            if r < t[a]:
                t[a] = r
                heapq.heappush(q, (r, a))

    return t

n, m = map(int, input().split())
s = int(input())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))

r = d(g, s, n)

for i in range(1, n + 1):
    print("INF" if r[i] == float('inf') else r[i])