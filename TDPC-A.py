# コンテスト

import sys
input = sys.stdin.readline


def S(): return input().rstrip()


def L(sep=' '): return list(S().split(sep=sep))


def I(): return int(input())


def IL(): return list(map(int, L()))


def IL2(n): return [IL() for _ in range(n)]


N = I()
p = IL()
MAX_VALUE = sum(p)

dp = [[False for _ in range(MAX_VALUE+1)] for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(MAX_VALUE+1):
        if dp[i][j] == True:
            dp[i+1][j] = True
        if dp[i][j-p[i]] == True:
            dp[i+1][j] = True
    # print(dp)
print(dp[N].count(True))
