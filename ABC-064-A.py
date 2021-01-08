# RGB-Cards

import sys
input = sys.stdin.readline


def S(): return input().rstrip()


def L(sep=' '): return list(S().split(sep=sep))


def I(): return int(input())


def IL(): return list(map(int, L()))


def IL2(n): return [IL() for _ in range(n)]


r, g, b = IL()
if (g*10 + b) % 4 == 0:
    print("YES")
else:
    print("NO")
