# Grid Repainting

from collections import deque
import sys
input = sys.stdin.readline

h, w = list(map(int, input().split()))
c = [list(input())[:-1] for _ in range(h)]


def bfs(start, goal, maze):
    sx, sy = start
    gx, gy = goal
    queue = deque([[sx, sy]])
    distance = [[-1 for i in range(w)] for j in range(h)]
    distance[sx][sy] = 0
    maze[sx][sy] = "#"
    dx_dy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    is_goal = False
    while queue:
        x, y = queue.popleft()
        d = distance[x][y]
        for i in range(4):
            nx, ny = x + dx_dy[i][0], y + dx_dy[i][1]
            if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] == ".":
                maze[nx][ny] = "#"
                distance[nx][ny] = d + 1
                queue.append([nx, ny])
            if [nx, ny] == [gx, gy]:
                is_goal = True
                break
        if is_goal:
            break
    if not is_goal:
        print(-1)
        sys.exit()
    return d + 1


s = [0, 0]
g = [h-1, w-1]
r = 0
for i in range(h):
    for j in range(w):
        if c[i][j] == ".":
            r += 1

d = bfs(s, g, c)
print(r - d - 1)
