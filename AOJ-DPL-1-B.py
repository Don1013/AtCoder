# Knapsack Problem

import sys
input = sys.stdin.readline


def S(): return input().rstrip()


def L(sep=' '): return list(S().split(sep=sep))


def I(): return int(input())


def IL(): return list(map(int, L()))


def IL2(n): return [IL() for _ in range(n)]


N, W = IL()
v = [0 for _ in range(N)]
w = [0 for _ in range(N)]
for i in range(N):
    v[i], w[i] = IL()

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(W+1):
        if j >= w[i]:  # 選ぶとき
            dp[i+1][j] = max(dp[i][j-w[i]] + v[i], dp[i][j])
        else:  # 選ばなかったとき
            dp[i+1][j] = dp[i][j]
    # print(dp)
print(dp[N][W])
