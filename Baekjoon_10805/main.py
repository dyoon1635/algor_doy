import sys
sys.setrecursionlimit(100000)

def rectangle(n, m):
    if rect[n][m] != INF: return rect[n][m]
    if n == m: return 1
    if n == 1: return m
    if m == 1: return n

    for i in range(1, n // 2 + 1):
        rect[n][m] = min(rect[n][m],
                         rectangle(i, m) + rectangle(n - i, m))
    for i in range(1, m // 2 + 1):
        rect[n][m] = min(rect[n][m],
                         rectangle(n, i) + rectangle(n, m - i))
    return rect[n][m]

def dp(n, m, x, y):
    if L[n][m][x][y] != INF: return L[n][m][x][y]
    #if x >= n or y >= m: return INF
    if x == 0 or y == 0: return rectangle(n, m)

    for i in range(1, n):
        if i < x:
            L[n][m][x][y] = min(L[n][m][x][y],
                                dp(n - i, m, x - i, y) + rectangle(i, m - y))
        elif i == x:
            L[n][m][x][y] = min(L[n][m][x][y],
                                rectangle(n - i, m) + rectangle(x, m - y))
        else:
            L[n][m][x][y] = min(L[n][m][x][y],
                                dp(i, m, x, y) + rectangle(n - i, m))
    for i in range(1, m):
        if i < y:
            L[n][m][x][y] = min(L[n][m][x][y],
                                dp(n, m - i, x, y - i) + rectangle(n - x, i))
        elif i == y:
            L[n][m][x][y] = min(L[n][m][x][y],
                                rectangle(n, m - i) + rectangle(n - x, y))
        else:
            L[n][m][x][y] = min(L[n][m][x][y],
                                dp(n, i, x, y) + rectangle(n, m - i))
    return L[n][m][x][y]

N, M, X, Y = map(int, input().split())

INF = N * M

rect =[[INF] * (M + 1) for _ in range(N + 1)]
L = [[[[INF] * (Y + 1) for _ in range(X + 1)]
      for _ in range(M + 1)] for _ in range(N + 1)]
print(dp(N, M, X, Y))