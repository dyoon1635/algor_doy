import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
bamboo = []
for _ in range(n):
    bamboo.append(list(map(int, input().split())))
result = [[-1] * n for _ in range(n)] # if -1 non-visited else visited
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def out_of_bound(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return True
    return False

def dfs(x, y):
    if result[x][y] != -1: return result[x][y]
    result[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if not out_of_bound(nx, ny):
            if bamboo[x][y] < bamboo[nx][ny]:
                result[x][y] = max(result[x][y],
                                   dfs(nx, ny) + 1)
    return result[x][y]

if __name__ == "__main__":
    res = 0
    for i in range(n):
        for j in range(n):
                res = max(res, dfs(i, j))
    print(res)