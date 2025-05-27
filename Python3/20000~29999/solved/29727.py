def pyliasec(n, r):
    if r > n:
        return 0
    ans = 1
    for i in range(n, n - r, -1):
        ans *= i
    for i in range(r, 0, -1):
        ans //= i
    return ans

def main():
    n = int(input())
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    
    tans = pyliasec(n + 1, 2)
    ans = tans * tans
    
    if xa == xb:
        if ya > yb:
            ya, yb = yb, ya
        
        if ya < n and yb >= 0:
            if ya < 0:
                ya = -1
            if yb > n:
                yb = n
            ans += pyliasec(yb - ya, 2) * (n + 1)
    
    elif ya == yb:
        if xa > xb:
            xa, xb = xb, xa
            
        if xa < n and xb >= 0:
            if xa < 0:
                xa = -1
            if xb > n:
                xb = n
            ans += pyliasec(xb - xa, 2) * (n + 1)
    
    print(ans)

if __name__ == "__main__":
    main()