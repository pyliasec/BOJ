import heapq

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
e = []
s = 0

for _ in range(m):
    x, y, z = map(int, input().split())
    a[x].append((y, z))
    a[y].append((x, z))
    e.append((x, y))
    s += z

p, q = map(int, input().split())

def dijkstra(start, n):
    h = [(0, start)]
    v = [float('inf')] * (n + 1)
    v[start] = 0
    while h:
        c, u = heapq.heappop(h)
        if v[u] < c:
            continue
        for w, k in a[u]:
            if v[w] > c + k:
                v[w] = c + k
                heapq.heappush(h, (v[w], w))
    return v

x = dijkstra(p, n)
y = dijkstra(q, n)

r = min(min(x[i] + y[j], x[j] + y[i]) for i, j in e)

print(s - r)