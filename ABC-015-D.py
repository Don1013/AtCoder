# 高橋くんの苦悩

import sys
input = sys.stdin.readline


def S(): return input().rstrip()


def L(sep=' '): return list(S().split(sep=sep))


def I(): return int(input())


def IL(): return list(map(int, L()))


def IL2(n): return [IL() for _ in range(n)]


W = I()
N, K = IL()
a = [0] * N
b = [0] * N
for i in range(N):
    a[i], b[i] = IL()

dp = [[[-1] * (K+1) for i in range(W+1)] for j in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    for w in range(W+1):
        for k in range(K+1):
            if dp[i][w][k] == -1:
                continue
            if k == K:  # 枚数制限に引っかかって貼れない
                dp[i+1][w][k] = max(dp[i][w][k], dp[i+1][w][k])
            else:
                if w + a[i] <= W:  # 幅の条件をクリアできるかどうか
                    dp[i+1][w+a[i]][k+1] = max(dp[i][w]
                                               [k] + b[i], dp[i+1][w+a[i]][k+1])  # 貼る
                    dp[i+1][w][k] = max(dp[i][w][k], dp[i+1][w][k])  # 貼らない
                else:
                    dp[i+1][w][k] = max(dp[i][w][k], dp[i+1][w][k])  # 貼れない
    # print(dp)

ans = 0
for w in range(W+1):
    ans = max(ans, max(dp[N][w]))
print(ans)
