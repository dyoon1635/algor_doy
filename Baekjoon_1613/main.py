import sys
inf = sys.maxsize
input = sys.stdin.readline

def solve():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

n, k = map(int, input().split())
dist = [[inf] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    dist[a][b] = 1

for i in range(1, n + 1): dist[i][i] = 0
solve()
for _ in range(int(input())):
    a, b = map(int, input().split())
    if dist[a][b] == inf and dist[b][a] == inf: print(0)
    elif dist[a][b] == inf: print(1)
    else: print(-1)