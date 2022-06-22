from collections import deque

n, m, k = map(int, input().split())
Map = []
for _ in range(n):
    Map.append(list(input()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def out_of_bound(x, y):
    if x < 0 or x >= n or \
        y < 0 or y >= m: return True
    return False

def solve():
    dq = deque()
    dq.append([0, 0, 0, 1]) # x, y, k, dist
    visited = [[[False for _ in range(m)] \
               for _ in range(n)] \
            for _ in range(k + 1)]
    visited[0][0][0] = True
    while dq:
        # current (x, y), k, distance
        cx, cy, ck, cd = dq.popleft()
        if (cx, cy) == (n - 1, m - 1):
            return cd

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if out_of_bound(nx, ny): continue

            if Map[nx][ny] == '0' \
                    and not visited[ck][nx][ny]:
                # road and not visited
                dq.append([nx, ny, ck, cd + 1])
                visited[ck][nx][ny] = True
            elif Map[nx][ny] == '1' and ck < k \
                    and not visited[ck + 1][nx][ny]:
                # wall and not visited + can break
                dq.append([nx, ny, ck + 1, cd + 1])
                visited[ck + 1][nx][ny] = True
    return -1

if __name__ == "__main__":
    print(solve())