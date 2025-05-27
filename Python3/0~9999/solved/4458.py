import sys
r = sys.stdin.buffer.readline
w = sys.stdout.buffer.write

n = int(r())
for _ in range(n):
    b = bytearray(r().rstrip(b'\n'))
    b[0] &= ~32
    w(b + b'\n')