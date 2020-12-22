# 深さ優先探索

from collections import deque
import sys
input = sys.stdin.readline

H, W = map(int, input().split(" "))
C = [list(input()) for _ in range(H)]

# スタートとゴールの設定
for i in range(H):
    for j in range(W):
        if C[i][j] == "s":
            sx, sy = i, j
        if C[i][j] == "g":
            gx, gy = i, j

stack = deque([[sx, sy]])
# 既に来た場所
visited = [[0 for i in range(W)] for j in range(H)]
visited[sx][sy] = 1

dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# 探索
while stack:
    x, y = stack.pop()
    for i in range(4):
        nx, ny = x+dx_dy[i][0], y+dx_dy[i][1]
        # 行けるか判定
        if 0 <= nx < W and 0 <= ny < H and visited[nx][ny] == 0 and C[nx][ny] != "#":
            visited[nx][ny] = 1
            stack.append([nx, ny])
        # ゴール判定
        if visited[gx][gy] == 1:
            print("Yes")
            sys.exit()

print("No")
