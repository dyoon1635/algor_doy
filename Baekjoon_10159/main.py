import sys

n, m  = int(input()), int(input())
adj = [[0] * n for _ in range(n)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    adj[x - 1][y - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if adj[i][k] and adj[k][j]: adj[i][j] = 1
for i in range(n):
    cnt = 0
    for j in range(n):
        if not adj[i][j] and not adj[j][i]: cnt += 1
    print(cnt - 1)