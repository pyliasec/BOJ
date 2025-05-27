n = int(input())
K = int(input())
sibal = list(map(int, input().split()))
sibal.sort()



d = []
for i in range(1, n) :
    
    d.append(sibal[i] - sibal[i - 1])

d.sort()

m = sum(d[:n - K])

print(m)