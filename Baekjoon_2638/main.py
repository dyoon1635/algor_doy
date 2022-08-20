from collections import deque
n, m = map(int, input().split())
cheese = []
for _ in range(n):
    cheese.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
size = 0
for i in range(n):
    for j in range(m):
        if cheese[i][j] == 1: size += 1

def out_of_bound(x, y):
    if x < 0 or x >= n or y < 0 or y >= m: return True
    return False

def bfs():
    global visited
    visited = [[False] * m for _ in range(n)]

    dq = deque()
    dq.append([0, 0])
    cheese[0][0] = 2
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not out_of_bound(nx, ny) and not visited[nx][ny] and cheese[nx][ny] != 1:
                visited[nx][ny] = True
                dq.append([nx, ny])
                cheese[nx][ny] = 2

def melt():
    global size
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                count = 0
                for dir in range(4):
                    nx, ny = i + dx[dir], j + dy[dir]
                    if not out_of_bound(nx, ny) and cheese[nx][ny] == 2:
                        count += 1
                if count >= 2: # count >= 1: 2636
                    cheese[i][j] = 0
                    size -= 1

if __name__ == "__main__":
    count = 0
    #size_record = [size] # 2636
    while size > 0:
        bfs()
        melt()
        count += 1
        #size_record.append(size) # 2636
    print(count)
    #print(size_record[-2]) # 2636

