N = int(input())
C = [[int(i) for i in input().split(" ")] for j in range(N)]


def calc_distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(1/2)


D = [0] * N**2
for i in range(N):
    for j in range(N):
        D[i*N + j] = calc_distance(C[i], C[j])

print(format(max(D), ".6f"))
