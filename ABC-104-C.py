# All Green

import sys
input = sys.stdin.readline

[D, G] = list(map(int, input()[:-1].split(" ")))
P = [0] * D
C = [0] * D
for i in range(D):
    [P[i], C[i]] = list(map(int, input()[:-1].split(" ")))

ans = 1e9
for i in range(2 ** D):
    cnt = 0
    score = 0
    rest_index = -1
    for j in range(D):
        if (i >> j) & 1:
            cnt += P[j]
            score += 100 * (j+1) * P[j] + C[j]
        else:
            rest_index = j
    if score < G:
        score1 = 100 * (rest_index + 1)
        need_cnt = (G - score + score1 - 1) // score1
        if need_cnt >= P[rest_index]:
            continue
        cnt += need_cnt
    if ans > cnt:
        ans = cnt

print(ans)
