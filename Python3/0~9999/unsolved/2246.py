# unsolved
def c(condo):
    sc = sorted(condo, key=lambda x: x[0])
    
    cc = 0
    m = float('inf')
    
    for d, c in sc:
        if c < m:
            cc += 1
            m = c
    
    return cc

N = int(input())
condo = [tuple(map(int, input().split())) for _ in range(N)]

print(c(condo))