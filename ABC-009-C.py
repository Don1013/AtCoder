# 辞書式順序ふたたび

import sys
input = sys.stdin.readline
import string

n, k = list(map(int, input().rstrip().split()))
s = input().rstrip()
slist = list(s)
tlist = sorted(slist)
ans = ""
solvable = False
for i in range(n):  # 全ての文字に対して
    res = []
    for j in tlist:
        ans += j
        cnt = k
        for l in range(i+1):
            if ans[l] != s[l]:
                cnt -= 1
            
        tlist.remove(j)
        slist = slist[1:]
        cnt += n - i - 1
        for l in list(string.ascii_lowercase):
            cnt -= max(slist.count(l), tlist.count(l))
        tlist.append(j)
        tlist.sort()
        if cnt >= 0:
            solvable = True
            tlist.remove(j)
            break
        else:
            ans = ans[:-1]
            slist = list(s)[i:]
    if solvable:
        pass
    else:
        print(-1)
        sys.exit()
        
print(ans)