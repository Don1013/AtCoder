# 派閥

import sys
input = sys.stdin.readline


def check_connection(habatsu, R):
    if len(habatsu) == 0:
        return False
    elif len(habatsu) == 1:
        return True
    need = [[habatsu[i], habatsu[j]]
            for i in range(len(habatsu)-1) for j in range(i+1, len(habatsu))]

    for i in range(len(need)):
        if need[i] in R:
            pass
        else:
            return False
    return True


[N, M] = list(map(int, input().split(" ")))
R = [list(map(int, input().split(" "))) for _ in range(M)]
ans = 0
for i in range(2 ** N):
    habatsu = []
    cnt = 0
    for j in range(N):
        if (i >> j) & 1:
            habatsu.append(j+1)
            cnt += 1

    if check_connection(habatsu, R):
        if ans < cnt:
            ans = cnt
print(ans)
