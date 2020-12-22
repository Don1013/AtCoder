# library
import sys
input = sys.stdin.readline


dx_dy = [[i, j] for i in [-1, 0, 1] for j in [-1, 0, 1]]


def dfs(x, y, id):
    visited[x][y] = id  # マーカー
    for i in range(9):
        nx, ny = x + dx_dy[i][0], y + dx_dy[i][1]  # 次点の決定
        if 0 <= nx < h and 0 <= ny < w and c[nx][ny] == 1 and visited[nx][ny] == -1:
            dfs(nx, ny, id)  # 再帰


while True:
    w, h = list(map(int, input().split()))
    if w or h:
        id = 0
        c = [list(map(int, input().split())) for _ in range(h)]
        visited = [[-1 if elem == 1 else elem for _, elem in enumerate(
            row)] for _, row in enumerate(c)]
        for x in range(h):
            for y in range(w):
                if c[x][y] == 1 and visited[x][y] == -1:
                    dfs(x, y, id)
                    id += 1
        print(id)
    else:
        break
