# チーズ

from collections import deque
import sys
input = sys.stdin.readline

h, w, n = list(map(int, input().split()))
c = [list(input())[:-1] for _ in range(h)]


def bfs(start, goal, maze, initial_d):
    sx, sy = start
    gx, gy = goal
    queue = deque([[sx, sy]])
    distance = [[-1 for i in range(w)] for j in range(h)]
    dx_dy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    distance[sx][sy] = initial_d
    is_goal = False
    while queue:
        x, y = queue.popleft()
        d = distance[x][y]
        for i in range(4):
            nx, ny = x + dx_dy[i][0], y + dx_dy[i][1]
            if 0 <= nx < h and 0 <= ny < w and distance[nx][ny] == -1 and maze[nx][ny] != "X":
                distance[nx][ny] = d + 1
                queue.append([nx, ny])
            if [nx, ny] == [gx, gy]:
                is_goal = True
                break
        if is_goal:
            break
    return d + 1


g = [[] for _ in range(n)]
for i in range(h):
    for j in range(w):
        if c[i][j] == "S":
            s = [i, j]
        elif c[i][j] != "." and c[i][j] != "X":
            g[int(c[i][j])-1] = [i, j]


d = 0
for i in range(n):
    d = bfs(s, g[i], c, d)
    s = g[i]
print(d)
