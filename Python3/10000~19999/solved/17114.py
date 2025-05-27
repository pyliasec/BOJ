from collections import deque

d = [
    (1,0,0,0,0,0,0,0,0,0,0), (-1,0,0,0,0,0,0,0,0,0,0),
    (0,1,0,0,0,0,0,0,0,0,0), (0,-1,0,0,0,0,0,0,0,0,0),
    (0,0,1,0,0,0,0,0,0,0,0), (0,0,-1,0,0,0,0,0,0,0,0),
    (0,0,0,1,0,0,0,0,0,0,0), (0,0,0,-1,0,0,0,0,0,0,0),
    (0,0,0,0,1,0,0,0,0,0,0), (0,0,0,0,-1,0,0,0,0,0,0),
    (0,0,0,0,0,1,0,0,0,0,0), (0,0,0,0,0,-1,0,0,0,0,0),
    (0,0,0,0,0,0,1,0,0,0,0), (0,0,0,0,0,0,-1,0,0,0,0),
    (0,0,0,0,0,0,0,1,0,0,0), (0,0,0,0,0,0,0,-1,0,0,0),
    (0,0,0,0,0,0,0,0,1,0,0), (0,0,0,0,0,0,0,0,-1,0,0),
    (0,0,0,0,0,0,0,0,0,1,0), (0,0,0,0,0,0,0,0,0,-1,0),
    (0,0,0,0,0,0,0,0,0,0,1), (0,0,0,0,0,0,0,0,0,0,-1)
]

def bfs(box):
    queue = deque()
    total_tomatoes = 0
    ripe_tomatoes = 0
    
    for w in range(W):
        for v in range(V):
            for u in range(U):
                for t in range(T):
                    for s in range(S):
                        for r in range(R):
                            for q in range(Q):
                                for p in range(P):
                                    for o in range(O):
                                        for n in range(N):
                                            for m in range(M):
                                                if box[w][v][u][t][s][r][q][p][o][n][m] != -1:
                                                    total_tomatoes += 1
                                                if box[w][v][u][t][s][r][q][p][o][n][m] == 1:
                                                    queue.append((w,v,u,t,s,r,q,p,o,n,m,0))
                                                    ripe_tomatoes += 1
    
    max_days = 0
    while queue:
        w, v, u, t, s, r, q, p, o, n, m, days = queue.popleft()
        max_days = max(max_days, days)
        
        for dw, dv, du, dt, ds, dr, dq, dp, do, dn, dm in d:
            nw, nv, nu, nt, ns, nr, nq, np, no, nn, nm = w+dw, v+dv, u+du, t+dt, s+ds, r+dr, q+dq, p+dp, o+do, n+dn, m+dm
            if 0 <= nw < W and 0 <= nv < V and 0 <= nu < U and 0 <= nt < T and 0 <= ns < S and \
               0 <= nr < R and 0 <= nq < Q and 0 <= np < P and 0 <= no < O and 0 <= nn < N and 0 <= nm < M:
                if box[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] == 0:
                    box[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] = 1
                    queue.append((nw,nv,nu,nt,ns,nr,nq,np,no,nn,nm,days+1))
                    ripe_tomatoes += 1
    
    return max_days if ripe_tomatoes == total_tomatoes else -1

M, N, O, P, Q, R, S, T, U, V, W = map(int, input().split())
box = [[[[[[[[[[list(map(int, input().split())) for _ in range(N)] for _ in range(O)] 
           for _ in range(P)] for _ in range(Q)] for _ in range(R)] for _ in range(S)]
           for _ in range(T)] for _ in range(U)] for _ in range(V)] for _ in range(W)]

print(bfs(box))