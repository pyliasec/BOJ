import heapq
from collections import defaultdict

def d(N, g, s, e):
    d = [[float('inf'), float('inf'), 0] for _ in range(N+1)]
    d[s] = [0, 0, 1]
    pq = [(0, 0, s)]

    while pq:
        dist, lines, n = heapq.heappop(pq)

        if n == e:
            return d[e]

        if dist > d[n][0] or (dist == d[n][0] and lines > d[n][1]):
            continue

        for nn, w in g[n]:
            new_dist = dist + w
            new_lines = lines + 1

            if new_dist < d[nn][0] or (new_dist == d[nn][0] and new_lines < d[nn][1]):
                d[nn] = [new_dist, new_lines, 0]
                heapq.heappush(pq, (new_dist, new_lines, nn))

            if new_dist == d[nn][0] and new_lines == d[nn][1]:
                d[nn][2] = (d[nn][2] + d[n][2]) % (10**9 + 9)

    return d[e]

N, M, x, y = map(int, input().split())
g = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    g[u].append((v, w))

r = d(N, g, x, y)

if r[0] == float('inf'):
    print(-1)
else:
    print(r[0])
    print(r[1])
    print(r[2])