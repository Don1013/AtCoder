# Robot Arms

n = int(input())
r = [list(map(int, input().rstrip().split())) for _ in range(n)]


def transpose(l):
    return list(list(x) for x in zip(*r))


r = transpose([sorted(l) for l in transpose(r)])
