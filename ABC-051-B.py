import sys
input = sys.stdin.readline


def input_to_int():
    return int(input())


def input_to_list():
    return input().split(" ")


def input_to_map(func):
    return map(func, input_to_list())


[K, S] = input_to_map(int)

cnt = 0
for x in range(K+1):
    for y in range(K+1):
        z = S - x - y
        if 0 <= z and z <= K:
            cnt += 1

print(cnt)
