import heapq
from collections import defaultdict
import sys

inf = sys.maxsize

def s(n, m, k, b):
    g = [[] for _ in range(n + 1)]
    for a, d, t, i in b:
        g[a].append((d, t, i))
    
    d = [inf] * (n + 1)
    d[1] = 0
    
    p = [(0, 1, k)]
    
    while p:
        t, u, c = heapq.heappop(p)
        
        if t != d[u]:
            continue
        
        for v, w, i in g[u]:
            if t % i == 0:
                nt = t + w
            else:
                nt = t + w + i - (t % i)

            if d[v] > nt:
                d[v] = nt
                heapq.heappush(p, (d[v], v, c))
            
            if c > 0:
                nt = t + w
                if d[v] > nt:
                    d[v] = nt
                    heapq.heappush(p, (d[v], v, c - 1))
    
    return d[n] if d[n] != inf else -1

n, m, k = map(int, sys.stdin.readline().split())
b = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
print(s(n, m, k, b))