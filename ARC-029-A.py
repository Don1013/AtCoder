# 高橋君とお肉
import sys
input = sys.stdin.readline

N = int(input())
T = [int(input()) for _ in range(N)]

ans = 1e9
for i in range(2 ** N):
    t1 = t2 = 0
    for j in range(N):
        if (i >> j) & 1:
            t1 += T[j]
        else:
            t2 += T[j]
    t = max([t1, t2])
    if t < ans:
        ans = t

print(ans)
