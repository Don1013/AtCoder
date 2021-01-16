# たくさんの数式

import sys
input = sys.stdin.readline


def S(): return input().rstrip()


def L(sep=' '): return list(S().split(sep=sep))


def I(): return int(input())


def IL(): return list(map(int, L()))


def IL2(n): return [IL() for _ in range(n)]


def main():
    s = S()
    n = len(s) - 1
    ans = 0
    for i in range(2 ** n):
        t = s[0]
        for j in range(n):
            if (i >> j) & 1:
                t += "+" + s[j+1]
            else:
                t += s[j+1]
        ans += sum(list(map(int, t.split(sep="+"))))

    print(ans)


main()
