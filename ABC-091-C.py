# 2D Place 2N Points

import sys
input = sys.stdin.readline


def S(): return input().rstrip()


def L(sep=' '): return list(S().split(sep=sep))


def I(): return int(input())


def IL(): return list(map(int, L()))


def IL2(n): return [IL() for _ in range(n)]


n = I()
r = IL2(n)
b = IL2(n)

r.sort()
b.sort()
ans = 0
for i in range(n):
    bx, by = b[i]
    cnd = []
    for j in range(len(r)):
        rx, ry = r[j]
        if rx < bx and ry < by:
            cnd.append([rx, ry])
    if len(cnd) > 0:
        # print(cnd)
        cnd.sort(key=lambda x: x[1], reverse=True)
        # print([bx, by], [cnd[0][0], cnd[0][1]])
        r.remove(cnd[0])
        ans += 1


print(ans)
