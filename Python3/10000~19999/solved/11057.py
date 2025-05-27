a = int(input())
b = 10007
c = [[0] * 10 for _ in range(a+1)]

for i in range(10):
    c[1][i] = 1

for i in range(2, a+1):
    for j in range(10):
        for k in range(j+1):
            c[i][j] += c[i-1][k]
        c[i][j] %= b

d = sum(c[a]) % b
print(d)