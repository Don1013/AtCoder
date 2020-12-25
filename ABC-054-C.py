# One-stroke Path

from itertools import permutations
import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
g = [tuple(map(int, input().rstrip().split())) for _ in range(m)]

cnt = 0
for i in permutations(list(range(1, n+1))):
    if i[0] != 1:
        continue
    flag = True
    for j in range(n-1):
        a, b = i[j], i[j+1]
        if (a, b) not in g and (b, a) not in g:
            flag = False
    if flag:
        cnt += 1

print(cnt)
