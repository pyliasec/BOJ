import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    s, t = map(int, input().split())

    time = 0
    count = 0

    while n > 0:
        if n == 1:
            time += s
            break
        if n % 2 == 0:
            if t < s * (n // 2):
                time += t
                n //= 2
            else:
                time += s * n
                break
        else:
            time += s
            n -= 1

    print(time)