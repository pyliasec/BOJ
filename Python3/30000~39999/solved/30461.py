import sys
input = sys.stdin.readline

def main():
    N, M, Q = map(int, input().split())
    
    fish = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    
    s = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + fish[i][j]
    
    for _ in range(Q):
        W, P = map(int, input().split())
        result = 0
        x, y = W, P
        
        while x > 0 and y > 0:
            result += s[x][y] - s[x][y-1] - s[0][y] + s[0][y-1]
            x -= 1
            y -= 1
        
        print(result)

if __name__ == "__main__":
    main()