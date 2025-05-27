n,s=input().split()
n=int(n)
a=[input().strip() for _ in range(n)]
a.sort(key=len)
u={s}
for w in a:
    if len(w)<=len(s): continue
    for i in range(len(w)):
        if w[:i]+w[i+1:] in u:
            u.add(w)
            break
print(max(u,key=len))