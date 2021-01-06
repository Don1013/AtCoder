# Saruman's army

import sys
input = sys.stdin.readline


def sarumans_army():
    while True:
        r, n = list(map(int, input().rstrip().split()))
        if r == n == -1:
            break
        x = list(map(int, input().rstrip().split()))
        x.sort()
        i = ans = 0
        while i < n:
            s = x[i]
            # print("start: {}".format(s))
            while i < n-1 and x[i+1] - s <= r:
                i += 1
            c = x[i]
            # print("center: {}".format(c))
            while i < n-1 and x[i+1] - c <= r:
                i += 1
            g = x[i]
            # print("goal: {}".format(g))
            ans += 1
            i += 1
        print(ans)


sarumans_army()
