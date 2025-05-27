x = input()
y = input()
s = ""
for i in range(0, len(x)):
    s += x[i] + y[i]

while len(s) != 2:
    t = ""
    for i in range(0, len(s) - 1):
        t += str((int(s[i]) + int(s[i + 1])) % 10)
    s = t
print(s)