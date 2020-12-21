import sys
input = sys.stdin.readline

[N, Y] = list(map(int, input().split()))

for x in range(N+1):
    for y in range(N+1):
        yen = Y - 10000 * x - 5000 * y
        z = N - x - y
        if 0 <= z and 1000 * z == yen:
            print(x, y, z)
            sys.exit()

print("-1 -1 -1")
