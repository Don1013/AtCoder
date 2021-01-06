# Multiple Gift

import sys
input = sys.stdin.readline


def S(): return input().rstrip()


def L(sep=" "): return list(S().split(sep=sep))


def I(): return int(input())


def IL(): return list(map(int, L()))


x, y = IL()
a = x
# print(a)
cnt = 1
while a*2 <= y:
    a *= 2
    # print(a)
    cnt += 1
print(cnt)
