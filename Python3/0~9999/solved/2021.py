from collections import deque
def f():
    n,l=map(int,input().split())
    m=[set()for _ in range(n+1)]
    t=[]
    for i in range(l):
        r=list(map(int,input().split()))
        r.pop()
        t.append(r)
        for s in r:
            m[s].add(i)
    a,b=map(int,input().split())
    if a==b:
        return 0
    q=deque([(a,0)])
    v=set([a])
    w=set()
    while q:
        c,d=q.popleft()
        for i in m[c]:
            if i in w:
                continue
            w.add(i)
            for s in t[i]:
                if s==b:
                    return d
                if s not in v:
                    v.add(s)
                    q.append((s,d+1))
    return -1
print(f())