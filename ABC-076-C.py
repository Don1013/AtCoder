# Dibious Document 2

import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

ns = len(s)
nt = len(t)

ans = []
for i in range(ns-nt+1):
    restorable = True
    for j in range(nt):
        if s[i+j] == t[j] or s[i+j] == "?":
            pass
        else:
            restorable = False
            break
    if restorable:
        ans.append(s.replace("?", "a")[:i] + t + s.replace("?", "a")[i+nt:])
        
if ans:
    print(min(ans))
else:
    print("UNRESTORABLE")