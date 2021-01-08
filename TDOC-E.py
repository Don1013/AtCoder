# 数
import sys
input = sys.stdin.readline


def S(): return input().rstrip()


def L(sep=' '): return list(S().split(sep=sep))


def I(): return int(input())


def IL(): return list(map(int, L()))


def IL2(n): return [IL() for _ in range(n)]


D = I()
N = S()
DIG = len(N)
MOD = int(1e9 + 7)

dp = [[[0] * D for _ in range(2)] for _ in range(DIG+1)]
dp[0][0][0] = 1

for i in range(DIG):
    n = int(N[i])
    for j in range(D):
        for k in range(10):
            dp[i+1][1][(j+k) % D] += dp[i][1][j]
            dp[i+1][1][(i+k) % D] %= MOD
        for k in range(n):
            dp[i+1][1][(j+k) % D] += dp[i][0][j]
            dp[i+1][1][(i+k) % D] %= MOD
        dp[i+1][0][(j+n) % D] = dp[i][0][j]
        dp[i+1][0][(j+n) % D] %= MOD
    # print(dp)

print(dp[DIG][0][0] + dp[DIG][1][0] - 1)
