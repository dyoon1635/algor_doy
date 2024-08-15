import sys, heapq
from collections import deque
sys.stdin.readline

def out_of_bound(x, y):
    return not (0 <= x < n and 0 <= y < m)

def get_island():
    result = 0
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and board[x][y]:
                result += 1
                bfs(x, y, result)
    return result

def bfs(x, y, num):
    dq = deque([(x, y)])
    visited[x][y], board[x][y] = True, num
    while dq:
        cx, cy = dq.popleft()
        for dir in range(4):
            nx, ny = cx + dx[dir], cy + dy[dir]
            if out_of_bound(nx, ny) or visited[nx][ny] or not board[nx][ny]:
                continue
            visited[nx][ny], board[nx][ny] = True, num
            dq.append((nx, ny))

def get_distance():
    for x in range(n):
        for y in range(m):
            if board[x][y]:
                start = board[x][y]
                for dir in range(4):
                    nx, ny, dist = x + dx[dir], y + dy[dir], 0
                    while not out_of_bound(nx, ny):
                        if board[nx][ny]:
                            end = board[nx][ny]
                            if start != end:
                                #print('heappush : ', x, y, ' : ', nx, ny, dist)
                                heapq.heappush(pq, (dist, start, end))
                            break
                        nx, ny, dist = nx + dx[dir], ny + dy[dir], dist + 1


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[max(x, y)] = min(x, y)

def printf():
    for each in board:
        print(each)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * m for _ in range(n)]

island_num = get_island()
parent = [i for i in range(island_num + 1)]
pq = []
get_distance()

result = 0
while pq:
    dist, s, e = heapq.heappop(pq)
    if dist == 1:
        continue
    ps, pe = find(s), find(e)
    if ps != pe:
        #print(s, e, dist)
        union(ps, pe)
        result += dist

connected = True
for each in parent[1:]:
    if parent[1] != parent[each]:
        connected = False
        break
print(-1 if result == 0 or not connected else result)