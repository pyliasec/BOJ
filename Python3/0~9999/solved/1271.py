def m1(n, m):
    m2 = n // m
    
    m3 = n % m
    
    return m2, m3

n, m = map(int, input().split())

m2, m3 = m1(n, m)

print(m2)
print(m3)