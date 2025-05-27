def S(arr):
    mx = float('-inf')
    cs = 0
    
    for num in arr:
        cs = max(num, cs + num)
        mx = max(mx, cs)
    
    return mx

while True:
    N = int(input())
    if N == 0:
        break
    
    p = [int(input()) for _ in range(N)]
    result = S(p)
    print(result)