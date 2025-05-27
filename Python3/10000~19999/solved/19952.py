import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    H, W, O, F, Xs, Ys, Xe, Ye = map(int, input().split())
    Xs, Ys, Xe, Ye = Xs - 1, Ys - 1, Xe - 1, Ye - 1
    grid = [[0] * W for _ in range(H)]
    for _ in range(O):
        x, y, L = map(int, input().split())
        grid[x - 1][y - 1] = L
    best = [[-1] * W for _ in range(H)]
    q = deque()
    best[Xs][Ys] = F
    q.append((Xs, Ys, F))
    reached = False
    while q:
        x, y, power = q.popleft()
        if x == Xe and y == Ye:
            reached = True
            break
        if power == 0:
            continue
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if grid[nx][ny] > grid[x][y] and power < grid[nx][ny] - grid[x][y]:
                continue
            newPower = power - 1
            if newPower <= best[nx][ny]:
                continue
            best[nx][ny] = newPower
            q.append((nx, ny, newPower))
    print("잘했어!!" if reached else "인성 문제있어??")