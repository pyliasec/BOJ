from heapq import heappush as h, heappop as p
from collections import defaultdict as d

def s():
    n, m, k, l, q = map(int, input().split())
    t = set(map(int, input().split()))

    g = d(list)
    for _ in range(m - l):
        a, b, c = map(int, input().split())
        g[a].append((b, c, False, False))
    for _ in range(l):
        a, b, c = map(int, input().split())
        g[a].append((b, c, True, False))
        g[b].append((a, c, True, True))

    u, v = map(int, input().split())

    d1 = d(lambda: d(lambda: float('inf')))
    d1[u][0] = 0
    pq = [(0, u, 0)]

    while pq:
        dist, cur, cnt = p(pq)
        if dist > d1[cur][cnt]:
            continue

        for n_v, n_w, trap, rev in g[cur]:
            n_d = dist + n_w
            n_c = (cnt + (n_v in t)) % (2 * q)

            if trap:
                if (cnt >= q and not rev) or (cnt < q and rev):
                    continue

            if n_d < d1[n_v][n_c]:
                d1[n_v][n_c] = n_d
                h(pq, (n_d, n_v, n_c))

    r = min(d1[v].values(), default=float('inf'))
    return r if r != float('inf') else -1

print(s())