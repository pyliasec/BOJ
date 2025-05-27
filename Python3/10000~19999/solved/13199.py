import sys
I=sys.stdin.readline
for _ in range(int(I())):
 P,M,F,C=map(int,I().split());b=M//P;t=b*C;print((b+max(0,(t-F)//(F-C)+1))-b-t//F if F>C else 0)