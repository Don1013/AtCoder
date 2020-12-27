# Clique Problem

import sys
input = sys.stdin.readline

n = int(input().rstrip())
l = [list(map(int, input().rstrip().split())) for _ in range(n)]
l = [[l[i][0]-l[i][1], l[i][0]+l[i][1]] for i in range(n)]
l.sort(key= lambda x:x[1])

ans = n
for i in range(1, n):
    if l[i-1][1] > l[i][0]:
        l[i][1] = l[i-1][1]
        ans -= 1
        
print(ans)