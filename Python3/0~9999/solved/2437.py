def a(n, w) :
    w.sort()
    mw = 0
    
    
    
    
    for wt in w :
        if wt > mw + 1 :
            return mw + 1
        mw += wt
    return mw + 1



N = int(input())
l = list(map(int, input().split()))

print(a(N, l))