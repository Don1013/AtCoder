# Robot Arms

import sys
input = sys.stdin.readline

n = int(input())
r = [list(map(int, input().rstrip().split())) for _ in range(n)]


def transpose(l):
    return list(list(x) for x in zip(*l))

r = [[e1 -e2, e1 + e2] for [e1, e2] in r]
r.sort(key = lambda x: x[1])

ans = n
for i in range(1, n):
    if r[i-1][1] > r[i][0]:
        r[i][1] = r[i-1][1]
        ans -= 1

print(ans)