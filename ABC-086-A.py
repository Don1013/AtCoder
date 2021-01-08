# Product

import sys
input = sys.stdin.readline


def S(): return input().rstrip()


def L(sep=' '): return list(S().split(sep=sep))


def I(): return int(input())


def IL(): return list(map(int, L()))


def IL2(n): return [IL() for _ in range(n)]


a, b = IL()
if (a * b) % 2 == 0:
    print("Even")
else:
    print("Odd")
