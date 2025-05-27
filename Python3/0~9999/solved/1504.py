import heapq
import sys

def d(g, s, e):
    dists = [float('inf')] * (n + 1)
    dists[s] = 0
    q = [(0, s)]

    while q:
        cd, cn = heapq.heappop(q)

        if cd > dists[cn]:
            continue

        for nn, w in g[cn]:
            dist = cd + w
            if dist < dists[nn]:
                dists[nn] = dist
                heapq.heappush(q, (dist, nn))

    return dists[e]

n, e = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))

v1, v2 = map(int, input().split())

d1v1 = d(g, 1, v1)
dv1v2 = d(g, v1, v2)
dv2n = d(g, v2, n)
d1v2 = d(g, 1, v2)
dv2v1 = d(g, v2, v1)
dv1n = d(g, v1, n)

p1 = d1v1 + dv1v2 + dv2n
p2 = d1v2 + dv2v1 + dv1n

res = min(p1, p2)

if res == float('inf'):
    print(-1)
else:
    print(res)