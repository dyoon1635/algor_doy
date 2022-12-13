from collections import deque

def out_of_bound(x, y):
    return x < 0 or x > n + 1 or y < 0 or y > m + 1

def bfs(x, y):
    global doc_count, board, key
    q = deque()
    q.append([x, y])
    while q:
        cx, cy = q.popleft()
        for dir in range(4):
            nx, ny = cx + dx[dir], cy + dy[dir]
            if out_of_bound(nx, ny) or visited[nx][ny] or \
                    board[nx][ny] == '*':
                continue

            if board[nx][ny].isalpha():
                if board[nx][ny].isupper():
                    idx = ord(board[nx][ny]) - 65
                    if key[idx]:
                        board[nx][ny] = '.'
                    else:
                        lock[idx].append([nx, ny])
                        continue
                else:
                    idx = ord(board[nx][ny]) - 97
                    if not key[idx]:
                        key[idx] = True
                        for X, Y in lock[idx]:
                            bfs(X, Y)

            if board[nx][ny] == '$':
                doc_count += 1
                board[nx][ny] = '.'
            visited[nx][ny] = True
            q.append([nx, ny])

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    board = []
    visited = [[False] * (m + 2) for _ in range(n + 2)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    key = [False for _ in range(26)]
    lock = [[] for _ in range(26)]
    board.append(['.' for _ in range(m + 2)])
    for _ in range(n):
        board.append(['.'] + list(input().strip()) + ['.'])
    board.append(['.' for _ in range(m + 2)])

    tmp = list(input().strip())
    for each in tmp:
        if each == '0': continue
        key[ord(each) - 97] = True
    doc_count = 0

    bfs(0, 0)
    print(doc_count)
