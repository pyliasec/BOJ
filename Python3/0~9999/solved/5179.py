class P:
    def __init__(self, id):
        self.id = id
        self.solved = set()
        self.score = 0
        self.wrong = {}

def proc_sub(p_list, p, m, t, j):
    if m not in p_list[p].solved:
        if j == 1:
            p_list[p].solved.add(m)
            p_list[p].score += t + p_list[p].wrong.get(m, 0) * 20
        else:
            p_list[p].wrong[m] = p_list[p].wrong.get(m, 0) + 1

def sort_p(p_list):
    return sorted(p_list.values(), key=lambda x: (-len(x.solved), x.score))

K = int(input())
for case in range(1, K + 1):
    M, N, P_cnt = map(int, input().split())
    p_list = {i: P(i) for i in range(1, P_cnt + 1)}
    
    for _ in range(N):
        p, m, t, j = input().split()
        proc_sub(p_list, int(p), m, int(t), int(j))
    
    sorted_p = sort_p(p_list)
    
    print(f"Data Set {case}:")
    for p in sorted_p:
        print(f"{p.id} {len(p.solved)} {p.score}")
    
    if case < K:
        print()
