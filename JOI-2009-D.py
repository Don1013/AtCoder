# カード並べ

from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
c = [input().rsplit()[0] for _ in range(n)]

ans = set()
for i in permutations(c, k):
    a = int("".join(i))
    ans.add(a)

print(len(ans))
