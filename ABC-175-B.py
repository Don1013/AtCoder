import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, [i for i in input().split(" ")]))
L.sort()

cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        Li = L[i]
        Lj = L[j]
        if Li == Lj:
            continue
        Lk_max = Li + Lj
        for k in range(j+1, N):
            Lk = L[k]
            if Lk < Lk_max and Lk != Lj:
                cnt += 1

print(cnt)
