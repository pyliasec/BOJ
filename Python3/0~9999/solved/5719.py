import sys
import heapq
from collections import defaultdict, deque

I = sys.stdin.readline
INF = float('inf')

def d(n, s, g):
    ds = [INF] * n
    ds[s] = 0
    h = []
    heapq.heappush(h, (0, s))
    p = [[] for _ in range(n)]
    
    while h:
        c, u = heapq.heappop(h)
        if c > ds[u]:
            continue
        for v, w in g[u]:
            nc = c + w
            if nc < ds[v]:
                ds[v] = nc
                heapq.heappush(h, (nc, v))
                p[v] = [u]
            elif nc == ds[v]:
                p[v].append(u)
    return ds, p

def r(n, s, e, g, p):
    q = deque()
    q.append(e)
    rm = [[False] * n for _ in range(n)]
    
    while q:
        u = q.popleft()
        if u == s:
            continue
        for v in p[u]:
            for i, (x, w) in enumerate(g[v]):
                if x == u and not rm[v][i]:
                    rm[v][i] = True
                    q.append(v)
    
    ng = defaultdict(list)
    for u in range(n):
        for i, (v, w) in enumerate(g[u]):
            if rm[u][i]:
                continue
            ng[u].append((v, w))
    return ng

def m():
    while True:
        n, m = map(int, I().split())
        if n == 0 and m == 0:
            break
        s, e = map(int, I().split())
        g = defaultdict(list)
        for _ in range(m):
            u, v, w = map(int, I().split())
            g[u].append((v, w))
        
        ds, p = d(n, s, g)
        
        if ds[e] == INF:
            print(-1)
            continue
        
        ng = r(n, s, e, g, p)
        
        ds2, _ = d(n, s, ng)
        print(ds2[e] if ds2[e] != INF else -1)

if __name__ == "__main__":
    m()