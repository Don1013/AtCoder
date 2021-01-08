# 暑い日々（Hot days）

import sys
input = sys.stdin.readline


def S(): return input().rstrip()


def L(sep=' '): return list(S().split(sep=sep))


def I(): return int(input())


def IL(): return list(map(int, L()))


def IL2(n): return [IL() for _ in range(n)]


D, N = IL()
T = [I() for _ in range(D)]
A = [0 for _ in range(N)]
B = [0 for _ in range(N)]
C = [0 for _ in range(N)]
for i in range(N):
    A[i], B[i], C[i] = IL()

dp = [[0] * N for _ in range(D)]

for d in range(1, D):
    for n in range(N):
        an, bn, cn = [A[n], B[n], C[n]]
        if T[d] < an or bn < T[d]:
            continue
        for pn in range(N):
            apn, bpn, cpn = [A[pn], B[pn], C[pn]]
            if T[d-1] < apn or bpn < T[d-1]:
                continue
            # print(cn, cpn)
            dp[d][n] = max(dp[d-1][pn] + abs(cn - cpn), dp[d][n])
    # print(dp)
print(max(dp[D-1]))
