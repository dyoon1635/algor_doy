import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

def out_of_bound(x, y):
    return not (0 < x <= n and 0 < y <= m)

def bfs():
    cost = [[[INF] * (3) for _ in range(m + 1)] for _ in range(n + 1)]
    cost[sx][sy][1] = 0
    pq = []
    heapq.heappush(pq, (0, sx, sy, 1)) # dist, x, y, k

    while pq:
        dist, cx, cy, ck = heapq.heappop(pq)
        if dist > cost[cx][cy][ck]: continue

        for dir in range(4):
            nx, ny, nk = cx + dx[dir], cy + dy[dir], (ck + 1) % 3
            if ck == 1 and cx == nx: continue # 상하이동
            if ck == 2 and cy == ny: continue # 좌우이동
            if out_of_bound(nx, ny) or board[nx][ny] == -1: continue
            next_dist = dist + board[nx][ny]
            if cost[nx][ny][nk] > next_dist:
                cost[nx][ny][nk] = next_dist
                heapq.heappush(pq, (next_dist, nx, ny, nk))
    return -1 if min(cost[ex][ey]) == INF else min(cost[ex][ey])

n, m = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())
board = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board.append([-1] * (m + 1))
for i in range(n):
    board.append([-1] + list(map(int, input().split())))
print(bfs())