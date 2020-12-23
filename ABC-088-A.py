# Infinite Coins

import sys
input = sys.stdin.readline

n = int(input())
a = int(input())

res = n % 500
if res <= a:
    print("Yes")
else:
    print("No")
