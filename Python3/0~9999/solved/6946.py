from collections import deque

def a():
    t = int(input())
    n = int(input())
    c = [int(input()) for _ in range(n)]

    INF = float('inf')
    s = [INF] * (t + 1)
    s[0] = 0

    q = deque([0])

    while q:
        cur = q.popleft()
        for x in c:
            nxt = cur + x
            if nxt > t:
                continue
            if s[nxt] == INF:
                s[nxt] = s[cur] + 1
                q.append(nxt)

    if s[t] != INF:
        print(f"Roberta wins in {s[t]} strokes.")
    else:
        print("Roberta acknowledges defeat.")

a()