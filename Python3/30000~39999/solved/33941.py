import sys
def main():
    input=sys.stdin.readline
    n=int(input())
    bs=0
    v=[]
    for _ in range(n):
        a=int(input())
        if a<=500 or a>=20000: continue
        y=(a-500)//10
        if y%50==0: bs+=y
        else: v.append(y)
    T=bs+sum(v)
    r=T%50
    if T==0 or (not v and r!=0):
        print(0); return
    if r==0:
        print(T*10); return
    inf=10**18
    d=[inf]*50
    d[0]=0
    for y in v:
        m=y%50
        od=d[:]
        for j in range(50):
            p=od[j]
            if p==inf: continue
            nj=(j+m)%50
            s=p+y
            if s<d[nj]: d[nj]=s
    s=d[r]
    if s>=inf:
        print(0)
    else:
        print((T-s)*10)

if __name__=='__main__':
    main()
