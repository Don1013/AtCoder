
# 器物損壊！高橋君

from collections import deque
import sys
input = sys.stdin.readline

h, w = list(map(int, input().split()))
c = [list(input().rstrip()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            sx, sy = [i, j]
        elif c[i][j] == "g":
            gx, gy = [i, j]

dx_dy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
score = [[1e5 for i in range(w)]for j in range(h)]


def bfs(start, maze):
    sx, sy = start
    score[sx][sy] = 0
    queue = deque([[sx, sy]])
    while queue:
        x, y = queue.popleft()
        cnt = score[x][y]
        for i in range(4):
            nx, ny = x + dx_dy[i][0], y + dx_dy[i][1]
            if 0 <= nx < h and 0 <= ny < w:
                if maze[nx][ny] != "#" and score[nx][ny] > cnt:
                    queue.appendleft([nx, ny])
                    score[nx][ny] = cnt
                elif maze[nx][ny] == "#" and score[nx][ny] > cnt + 1:
                    queue.append([nx, ny])
                    score[nx][ny] = cnt + 1


bfs([sx, sy], c)
print("YNEOS"[not(score[gx][gy] < 3)::2])
