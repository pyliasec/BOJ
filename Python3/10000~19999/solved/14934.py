a = int(input())
b = 10**a
c = pow(5, a, b)
print(6 if pow(c+1, a, b) > b//2 else 5)