# Duplex Printing

import sys
input = sys.stdin.readline


def S(): return input().rstrip()


def L(sep=' '): return list(S().split(sep=sep))


def I(): return int(input())


def IL(): return list(map(int, L()))


def IL2(n): return [IL() for _ in range(n)]


def main():
    n = I()
    if n % 2 == 0:
        print(int(n/2))
    else:
        print(int(n//2 + 1))


main()
