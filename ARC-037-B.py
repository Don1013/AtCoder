# バウムテスト
# library
import sys

# Type Alias
# Input


def input(): return sys.stdin.readline().strip()  # 高速なinput()に再定義


def I() -> int: return int(input())  # 単独の整数


def LI(): return list(map(int, input().split()))  # 整数のベクトル（一行、一次元配列）


def IR(n: int): return [I() for _ in range(n)]  # 整数のリスト（n行、一次元配列）


def LIR(n: int): return [LI() for _ in range(n)]  # 整数のベクトルのリスト（n行、二次元配列）


def S() -> str: return input()  # 文字列


def SR(n: int): return [S() for _ in range(n)]  # 文字列のリスト（n行、一次元配列）


def LS() -> list: return input().split()  # 文字のリスト（一行、一次元配列）
###


n, m = LI()
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v = LI()
    u, v = u - 1, v - 1
    edges[u].append(v)
    edges[v].append(u)

visited = set()


def dfs(now, prev):
    global is_tree
    visited.add(now)
    for v in edges[now]:
        if v != prev:
            if v in visited:
                is_tree = False
            else:
                visited.add(v)
                dfs(v, now)


ans = 0
for i in range(n):
    if i not in visited:
        is_tree = True
        dfs(i, -1)
        if is_tree:
            ans += 1

print(ans)


# N, M = list(map(int, input().split()))
# A = [list(map(int, input().split())) for _ in range(M)]
# visited = set()
# stack = deque([1])
# cnt = 0
# while stack:
#     nn = stack.pop()
#     visited.add(nn)
#     flag = True
#     for i in range(M):
#         if A[i][0] == nn:
#             if A[i][1] not in visited:
#                 stack.append(A[i][1])
#             else:
#                 flag = False
#     if not stack and flag:
#         cnt += 1
#         if nn != N:
#             for j in range(1, N+1):
#                 if not j in visited:
#                     stack.append(j)
#                     break
#
#
# print(cnt)
#
