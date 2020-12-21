import sys
input = sys.stdin.readline

S = input()[:-1]
n = len(S) - 1
ans = 0
for i in range(2**n):
    s = S[0]
    for j in range(n):
        if (i >> j) & 1:
            s = "+".join([s, S[j+1]])
        else:
            s = "".join([s, S[j+1]])

    l = [int(i) for i in s.split("+")]
    ans += sum(l)

print(ans)
