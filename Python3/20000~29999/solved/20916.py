import sys
from collections import Counter
input = sys.stdin.readline
targets = [202021, 20202021] + [202000000 + i * 10000 + 2021 for i in range(10)]
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    cnt = Counter(A)
    ans = 0
    for S in targets:
        for x, c in cnt.items():
            y = S - x
            if y in cnt:
                if x < y:
                    ans+=c*cnt[y]
                elif x == y:
                    ans += c * (c - 1) // 2
    print(ans)