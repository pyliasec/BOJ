import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n,r = map(int,input().split())
w = [0]+list(map(int,input().split()))
e = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u,v = map(int,input().split())
    e[u].append(v)
    e[v].append(u)
ch = [[] for _ in range(n + 1)]
par = [0]*(n+1)
stk = [r]
while stk:
    u = stk.pop()
    for v in e[u]:
        if v == par[u]: continue
        par[v] = u
        ch[u].append(v)
        stk.append(v)
dp = {}
def f(u,s):
    if (u,s) in dp: return dp[(u,s)]
    a = w[u]
    for v in ch[u]: a += f(v,u)
    b = w[u]-w[s]
    for v in ch[u]: b += f(v,s)
    dp[(u,s)]=a if a<b else b
    return dp[(u,s)]
res = w[r]
for v in ch[r]: res += f(v,r)
print(res)