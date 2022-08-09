from collections import deque

n, l, r = map(int, input().split())
country = []
for _ in range(n):
    country.append(list(map(int, input().split())))
visited = [[False] * n for _ in range(n)]
check = False

def out_of_bound(x, y):
    if x < 0 or x >= n or y < 0 or y >= n: return True
    return False

def imigration(union):
    global check
    check = True
    population = 0
    for x, y in union:
        population += country[x][y]
    population = int(population / len(union))
    for x, y in union:
        country[x][y] = population

def bfs(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    union = [[x, y]]
    dq = deque()
    dq.append([x, y])
    while dq:
        row, col = dq.popleft()
        for i in range(4):
            nx, ny = row + dx[i], col + dy[i]
            if not out_of_bound(nx, ny) and not visited[nx][ny]:
                diff = abs(country[nx][ny] - country[row][col])

                if l <= diff <= r:
                    visited[nx][ny] = True
                    dq.append([nx, ny])
                    union.append([nx, ny])
    if len(union) > 1: imigration(union)

def solve():
    global visited
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                visited[x][y] = True
                bfs(x, y)
    return check

if __name__ == "__main__":
    day = 0
    while True:
        check = False
        if not solve() or day >= 2000: break
        day += 1
    print(day)