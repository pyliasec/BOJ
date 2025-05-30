def s(m, x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            m[i][j] = '1' if m[i][j] == '0' else '0'

def main():
    N, M = map(int, input().split())
    A = [list(input().strip()) for _ in range(N)]
    B = [list(input().strip()) for _ in range(N)]

    c = 0

    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                s(A, i, j)
                c += 1

    if A == B:
        print(c)
    else:
        print(-1)

if __name__ == "__main__":
    main()
