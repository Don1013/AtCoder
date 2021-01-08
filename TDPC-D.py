# サイコロ

import sys
input = sys.stdin.readline


def S(): return input().rstrip()


def L(sep=' '): return list(S().split(sep=sep))


def I(): return int(input())


def IL(): return list(map(int, L()))


def IL2(n: int): return [IL() for _ in range(n)]


n, d = IL()

cnt2 = cnt3 = cnt5 = 0
while d % 2 == 0:
    d /= 2
    cnt2 += 1
while d % 3 == 0:
    d /= 3
    cnt3 += 1
while d % 5 == 0:
    d /= 5
    cnt5 += 1

if d != 1:
    print(0)
    sys.exit()

# dp[i][c2][c3][c5]: i番目までの積に含まれる素因数2,3,5の個数がc2,c3,c5である確率
dp = [[[[0 for i in range(cnt5+1)] for j in range(cnt3+1)]
       for k in range(cnt2+1)] for l in range(n+1)]
dp[0][0][0][0] = 1

dice2 = [0, 1, 0, 2, 0, 1]
dice3 = [0, 0, 1, 0, 0, 1]
dice5 = [0, 0, 0, 0, 1, 0]

for i in range(n):
    for c2 in range(cnt2+1):
        for c3 in range(cnt3+1):
            for c5 in range(cnt5+1):
                for j in range(6):
                    nc2 = min(cnt2, c2+dice2[j])  # cnt2で頭打ちにするようにminを付ける
                    nc3 = min(cnt3, c3+dice3[j])
                    nc5 = min(cnt5, c5+dice5[j])
                    dp[i+1][nc2][nc3][nc5] += dp[i][c2][c3][c5] / 6
    # print(dp)

print(dp[n][cnt2][cnt3][cnt5])
