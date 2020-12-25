# Cup

from collections import deque
import sys
input = sys.stdin.readline


def move(cup):
    if:
        return 0
    elif


while True:
    n, m = list(map(int, input().split()))
    if n == m == 0:
        sys.exit()
    cup = [0] * 3
    for i in range(3):
        t = input().rstrip()
        if t != "0":
            k, t = t.split(" ", 1)
            c = list(map(int, t.split()))
            for j in c:
                cup[i] += 1 << j-1
    print(list(map(lambda x: bin(x), cup)))


bfs()
