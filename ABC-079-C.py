# Train Ticket

import sys
input = sys.stdin.readline

s = input()[:-1]
n = len(s) - 1

for i in range(2 ** n):
    t = s[0]
    ans = int(s[0])
    for j in range(n):
        if (i >> j) & 1:
            t = "+".join([t, s[j+1]])
            ans += int(s[j+1])
        else:
            t = "-".join([t, s[j+1]])
            ans -= int(s[j+1])

    if ans == 7:
        print("=".join([t, "7"]))
        sys.exit()
