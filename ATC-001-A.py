# 深さ優先探索
import sys
input = sys.stdin.readline

[H, W] = list(map(int, input().split(" ")))
C = [list(input())[:-1] for _ in range(H)]
