# 幅優先探索
from collections import deque
import sys
input = sys.stdin.readline

r, c = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
sy, sx = sy - 1, sx - 1
gy, gx = list(map(int, input().split()))
gy, gx = gy - 1, gx - 1
maze = [list(input())[:-1] for _ in range(r)]

queue = deque([[sy, sx]])
dx_dy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
distance = [[-1 for i in range(c)] for j in range(r)]  # 距離を記録する配列


def bfs(sx, sy, maze):
    queue = deque([[sy, sx]])
    distance[sy][sx] = 0  # スタートの距離は0
    while queue:
        y, x = queue.popleft()
        d = distance[y][x]  # 位置(y, x)のスタートからの距離dを呼び出す
        for i in range(4):
            ny, nx = y + dx_dy[i][0], x + dx_dy[i][1]
            if 0 <= ny < r and 0 <= nx < c and maze[ny][nx] != "#":
                maze[ny][nx] = "#"
                queue.append([ny, nx])
                distance[ny][nx] = d + 1  # (ny, nx)のスタートからの距離は(x, y)より1多い
            if [gy, gx] == [ny, nx]:  # ゴールしたら終了
                print(d + 1)
                sys.exit()


bfs(sy, sy, maze)
