import sys

def a():
    while True:
        b = int(sys.stdin.readline())
        if b == 0:
            break
        c = [int(sys.stdin.readline()) for _ in range(b)]
        c.sort()
        
        d = 0
        for e in c:
            if e <= d:
                d = e + 200
            else:
                break
        
        if d >= 1422:
            d -= 1422
            if d >= 1422 - c[-1]:
                print("POSSIBLE")
            else:
                print("IMPOSSIBLE")
        else:
            print("IMPOSSIBLE")

if __name__ == "__main__":
    a()
