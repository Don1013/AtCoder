# カードゲーム

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

win = dorl = 0
for i in permutations(a):
    for j in permutations(b):
        wa = wb = 0
        print(i, j)
        for k in range(n):
            if i[k] > j[k]:
                print(i[k], j[k])
                wa += 1
            elif i[k] < j[k]:
                wb += 1
        if wa > wb:
            print("win")
            win += 1
        else:
            dorl += 1

print(win / (win + dorl))
