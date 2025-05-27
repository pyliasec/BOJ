import heapq as h
import sys
r=sys.stdin.readline
I=float('inf')

def f(g,s,n):
    d=[I]*(n+1)
    d[s]=0
    q=[(0,s)]
    while q:
        c,u=h.heappop(q)
        if c>d[u]:continue
        for v,w in g[u]:
            t=c+w
            if t<d[v]:
                d[v]=t
                h.heappush(q,(t,v))
    return d

def w(g,s,n):
    d=[[I,I]for _ in range(n+1)]
    d[s][0]=0
    q=[(0,s,0)]
    while q:
        c,u,e=h.heappop(q)
        if c>d[u][e]:continue
        for v,w in g[u]:
            if e==0:
                t=c+w/2
                if t<d[v][1]:
                    d[v][1]=t
                    h.heappush(q,(t,v,1))
            else:
                t=c+w*2
                if t<d[v][0]:
                    d[v][0]=t
                    h.heappush(q,(t,v,0))
    return [min(x)for x in d]

def s():
    n,m=map(int,r().split())
    g=[[]for _ in range(n+1)]
    for _ in range(m):
        a,b,d=map(int,r().split())
        g[a].append((b,d))
        g[b].append((a,d))
    x=f(g,1,n)
    y=w(g,1,n)
    return sum(1 for i in range(1,n+1)if x[i]<y[i])

print(s())