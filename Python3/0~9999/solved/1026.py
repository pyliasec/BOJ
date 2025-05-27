n = int(input())
a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))
tmp = sorted(b, reverse = True)
tmp1 = 0
for i in range(n):
    tmp1 += a[i] * tmp[i]
    
print(tmp1)