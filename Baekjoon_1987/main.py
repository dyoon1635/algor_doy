r, c = map(int, input().split())
board = []
alphabet = [False] * 26
visited = [[False] * c for _ in range(r)]
for _ in range(r):
    board.append(list(input().rstrip()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 1

def out_of_bound(x, y):
    return x < 0 or x >= r or y < 0 or y >= c

def backtracking(x, y, s):
    global answer
    answer = max(answer, s)
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if out_of_bound(nx, ny) or \
                visited[nx][ny] or \
                alphabet[ord(board[nx][ny]) - ord('A')]:
            continue

        visited[nx][ny] = True
        alphabet[ord(board[nx][ny]) - ord('A')] = True
        backtracking(nx, ny, s + 1)
        visited[nx][ny] = False
        alphabet[ord(board[nx][ny]) - ord('A')] = False

visited[0][0] = True
alphabet[ord(board[0][0]) - ord('A')] = True
backtracking(0, 0, 1)
print(answer)
