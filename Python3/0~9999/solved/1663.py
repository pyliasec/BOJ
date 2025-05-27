def i():
    N = 100
    d = [[0]*3 for _ in range(N+1)]
    d[1] = [1, 0, 0]
    d[2] = [0, 1, 1]
    d[3] = [1, 0, 1]

    for i in range(4, N+1):
        for j in range(3):
            d[i][j] = d[i-2][j] + d[i-3][j]
    
    return d

def a(d, n):
    return sum(d[n])

def b(d, n, k):
    while n >= 4:
        if sum(d[n-3]) >= k:
            n -= 3
        else:
            k -= sum(d[n-3])
            n -= 2
    
    if (n == k == 1) or (n == 3 and k == 2):
        return 'X'
    elif n == 2 and k == 1:
        return 'Y'
    else:
        return 'Z'

def c(d, n, h):
    j = ord(h) - ord('X')
    return d[n][j]

def m():
    d = i()
    
    t = int(input())
    n = int(input())
    
    if t == 1:
        print(a(d, n))
    elif t == 2:
        k = int(input())
        print(b(d, n, k))
    else:
        h = input()
        print(c(d, n, h))

if __name__ == "__main__":
    m()