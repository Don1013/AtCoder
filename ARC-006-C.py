import sys
input = sys.stdin.readline


def S(): return input().rstrip()


def L(sep=' '): return list(S().split(sep=sep))


def I(): return int(input())


def IL(): return list(map(int, L()))


n = I()
box = [1e10]
for i in range(n):
    w = I()
    stacked = False
    for i in range(len(box)):
        if w <= box[i]:
            box[i] = w
            stacked = True
            break
    if not stacked:
        box.append(w)
    # print(box)
print(len(box))
