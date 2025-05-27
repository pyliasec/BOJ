import re

def number(text):
    return [int(num) for num in re.findall(r'\d+', text)]

N = int(input())
n = []

for _ in range(N):
    line = input()
    n.extend(number(line))

n.sort()

for num in n:
    print(num)