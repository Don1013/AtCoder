# Island War

import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
l = [list(map(int, input().rstrip().split())) for _ in range(m)]
l.sort(key=lambda x: x[1])

ans = m
for i in range(1, m):
    if l[i-1][1] > l[i][0]:
        l[i][1] = l[i-1][1]
        ans -= 1
        
print(ans)