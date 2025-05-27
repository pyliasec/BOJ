def find_exam_time(N, M, S, e):
    e = [(x, x+y) for x, y in e]
    e.sort()

    if e[0][0] >= M:
        return 0

    for i in range(1, N):
        if e[i][0] - e[i-1][1] >= M:
            return e[i-1][1]

    if S - e[-1][1] >= M:
        return e[-1][1]

    return -1

N, M, S = map(int, input().split())
e = [tuple(map(int, input().split())) for _ in range(N)]

result = find_exam_time(N, M, S, e)
print(result)