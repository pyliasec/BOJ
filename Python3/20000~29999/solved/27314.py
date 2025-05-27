from collections import deque

def bfs(grid, starts, N, M):
    q = deque(starts)
    dist = [[-1] * M for _ in range(N)]
    
    for x, y in starts:
        dist[x][y] = 0
    
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != 'X' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    
    return dist

def max_gifts(N, M, grid):
    h, exits, people = None, [], []
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'H':
                h = (i, j)
            elif grid[i][j] == '#':
                exits.append((i, j))
            elif grid[i][j] == 'P':
                people.append((i, j))
    
    hanbyeol_dist = bfs(grid, [h], N, M)
    people_dist_map = {p: bfs(grid, [p], N, M) for p in people}
    
    max_gifts = 0
    for ex, ey in exits:
        if hanbyeol_dist[ex][ey] == -1:
            continue
        
        count = sum(0 <= people_dist_map[p][ex][ey] <= hanbyeol_dist[ex][ey] for p in people)
        max_gifts = max(max_gifts, count)
    
    return max_gifts

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]
print(max_gifts(N, M, grid))