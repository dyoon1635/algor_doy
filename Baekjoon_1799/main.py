import sys
input = sys.stdin.readline

def is_black(x, y):
    # (0, 0)부터 Black
    return True if (x + y) % 2 == 0 else False

def set_bishop(x, y, eps):
    for i in range(n):
        if 0 <= x - i < n and 0 <= y - i < n:
            check_board[x - i][y - i] += eps
        if 0 <= x - i < n and 0 <= y + i < n:
            check_board[x - i][y + i] += eps
        if 0 <= x + i < n and 0 <= y - i < n:
            check_board[x + i][y - i] += eps
        if 0 <= x + i < n and 0 <= y + i < n:
            check_board[x + i][y + i] += eps

def backtracking(idx, cnt):
    global answer
    if idx >= len(bishop):
        answer = max(answer, cnt)
        return

    x, y = bishop[idx]
    if not check_board[x][y]:
        set_bishop(x, y, 1)
        backtracking(idx + 1, cnt + 1)
        set_bishop(x, y, -1)
        backtracking(idx + 1, cnt)
    else: backtracking(idx + 1, cnt)

n = int(input())
board = []
black, white = [], []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j]:
            if is_black(i, j): black.append((i, j))
            else: white.append((i, j))
    board.append(tmp)
check_board = [[0] * n for _ in range(n)]

answer, total = 0, 0
bishop = black
backtracking(0, 0)
total += answer

answer = 0
bishop = white
backtracking(0, 0)
total += answer

print(total)