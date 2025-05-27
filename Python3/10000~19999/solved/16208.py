import heapq

def f(a, b):
    c = b[:]
    heapq.heapify(c)
    
    d = 0
    
    while len(c) > 1:
        x = heapq.heappop(c)
        y = heapq.heappop(c)
        
        e = x * y
        d += e
        
        heapq.heappush(c, x + y)
    
    return d

a = int(input())
b = list(map(int, input().split()))

print(f(a, b))