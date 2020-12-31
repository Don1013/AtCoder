# Best Cow Line

import sys
input = sys.stdin.readline

n = int(input())
s = "".join([input().rstrip() for _ in range(n)])

l = 0
e = n-1
ans = ""

while l <= e:
    is_end = False
    for i in range(e-l+1):  # 0 <= i <= e - l
        if s[l+i] > s[e-i]:
            is_end = True
            break
        if s[l+i] < s[e-i]:
            break
    
    if is_end:
        ans += s[e]
        e -= 1
    else:
        ans += s[l]
        l += 1
print(ans)