import sys
input = sys.stdin.readline

def aaa(T, a, N):
    left = -10**18
    right = 10**18
    for j, aj in enumerate(a, start=1):
        d = T // aj
        low = j - d
        high = j + d
        if low > left:
            left = low
        if high < right:
            right = high
        if left > right:
            return False
    return not (right < 1 or left > N)

N = int(input())
a = list(map(int, input().split()))

hi = 0
for j, aj in enumerate(a, start=1):
    hi = max(hi, (j-1)*aj, (N-j)*aj)

lo = 0
while lo < hi:
    mid = (lo + hi) // 2
    if aaa(mid, a, N):
        hi = mid
    else:
        lo = mid + 1

print(lo)
