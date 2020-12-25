# おつり

import sys
input = sys.stdin.readline

c = 1000 - int(input())
ans = 0
while c != 0:
    if c >= 500:
        c -= 500
    elif c >= 100:
        c -= 100
    elif c >= 50:
        c -= 50
    elif c >= 10:
        c -= 10
    elif c >= 5:
        c -= 5
    elif c >= 1:
        c -= 1
    ans += 1

print(ans)
