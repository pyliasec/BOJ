n,k = map(int, input().split())

a = 1
for i in range(2, n+1):
    a = ((a + k - 1) % i) + 1
    
print(a)