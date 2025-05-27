def C(N, M, m):
    m.sort()
    count = 0
    left = 0
    right = N - 1

    while left < right:
        c = m[left] + m[right]
        if c == M:
            count += 1
            left += 1
            right -= 1
        elif c < M:
            left += 1
        else:
            right -= 1

    return count

N = int(input())
M = int(input())
m = list(map(int, input().split()))

result = C(N, M, m)
print(result)