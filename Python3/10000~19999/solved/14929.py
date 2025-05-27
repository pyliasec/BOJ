n = int(input())
x = list(map(int, input().split()))

sum_x = sum(x)
ss = sum(xi**2 for xi in x)

result = (sum_x**2 - ss) // 2

print(result)