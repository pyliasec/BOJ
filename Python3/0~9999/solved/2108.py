import sys
from collections import Counter

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

mean = round(sum(numbers) / N)

s = sorted(numbers)
median = s[N // 2]

count = Counter(numbers)
mode = sorted(count.items(), key=lambda x: (-x[1], x[0]))[0][0]
if len(count) > 1 and count[mode] == count[sorted(count.items(), key=lambda x: (-x[1], x[0]))[1][0]]:
    mode = sorted(count.items(), key=lambda x: (-x[1], x[0]))[1][0]

range_value = max(numbers) - min(numbers)

print(mean)
print(median)
print(mode)
print(range_value)