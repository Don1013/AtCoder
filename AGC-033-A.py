# Darker and Darker

from collections import deque
import sys
input = sys.stdin.readline

h, w = list(map(int, input().split()))
a = [list(input())[:-1] for _ in range(h)]

distance = [[0 if elem == "#" else -1 for _,
             elem in enumerate(row)] for _, row in enumerate(a)]
queue = deque([[i, j] for i, row in enumerate(a)
               for j, elem in enumerate(row) if elem == "#"])
dx_dy = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(maze):
    while queue:
        x, y = queue.popleft()
        maze[x][y] = "#"
        d = distance[x][y]
        for j in range(4):
            nx, ny = x + dx_dy[j][0], y + dx_dy[j][1]
            if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] == ".":
                queue.append([nx, ny])
                maze[nx][ny] = "#"
                distance[nx][ny] = d + 1
    return d


print(bfs(a))
