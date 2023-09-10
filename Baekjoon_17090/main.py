import sys
sys.setrecursionlimit(600000)

def out_of_bound(x, y):
    return not (0 <= x < n and 0 <= y < m)

def dfs(x, y):
    global possible
    if out_of_bound(x, y):
        possible = True
        return
    if visited[x][y][0]: # already visited
        if visited[x][y][1]: # possible route
            possible = True
        return

    visited[x][y][0] = True
    if board[x][y] == 'U': dfs(x - 1, y)
    elif board[x][y] == 'D': dfs(x + 1, y)
    elif board[x][y] == 'L': dfs(x, y - 1)
    elif board[x][y] == 'R': dfs(x, y + 1)

    if possible: visited[x][y][1] = True

n, m = map(int, input().split())
visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
board = []
for _ in range(n):
    board.append(list(input().strip()))

result = 0
for i in range(n):
    for j in range(m):
        if visited[i][j][0]: # already visited
            if visited[i][j][1]: result += 1 # possible route
            continue
        else:
            possible = False
            dfs(i, j)
            if possible: result += 1
print(result)
