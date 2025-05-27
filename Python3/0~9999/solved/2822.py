s = [int(input()) for _ in range(8)]

ss = list(enumerate(s, start=1))

ss.sort(key=lambda x: x[1], reverse=True)

ts = sum(score for _, score in ss[:5])

t = sorted([index for index, _ in ss[:5]])

print(ts)
print(' '.join(map(str, t)))