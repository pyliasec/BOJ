def s(N):
    for i in range((N // 5), -1, -1):
        r = N - (5 * i)
        if r % 3 == 0:
            return i + (r // 3)
    return -1

N = int(input())

print(s(N))