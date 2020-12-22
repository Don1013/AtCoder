# 埋め立て

from collections import deque
import sys
from copy import deepcopy
input = sys.stdin.readline

A = [list(input())[:-1] for _ in range(10)]
flag = False
for i in range(10):
    for j in range(10):
        if A[i][j] == "o":
            sx, sy = i, j
            flag = True
            break
    if flag:
        break

dx_dy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for i in range(10):
    for j in range(10):
        if A[i][j] == "x":
            a = deepcopy(A)
            a[i][j] = "o"
            stack = deque([[sx, sy]])
            visited = [
                [1 if A[i][j] == "x" else 0 for j in range(10)] for i in range(10)]
            visited[i][j] = 0
            while stack:
                x, y = stack.pop()
                for k in range(4):
                    nx, ny = x + dx_dy[k][0], y + dx_dy[k][1]
                    # print(k, x, y, nx, ny)
                    if 0 <= nx < 10 and 0 <= ny < 10 and a[nx][ny] == "o" and visited[nx][ny] == 0:
                        stack.append([nx, ny])
                        visited[nx][ny] = 1
            if visited == [[1 for j in range(10)] for i in range(10)]:
                print("YES")
                sys.exit()

print("NO")
