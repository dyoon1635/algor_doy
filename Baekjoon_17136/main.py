import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def out_of_bound(x, y):
    return not (0 <= x < 10 and 0 <= y < 10)

def is_fill_with_value(x, y, k, value):
    for i in range(x, x + k + 1):
        for j in range(y, y + k + 1):
            if board[i][j] != value:
                return False
    return True

def fill(x, y, k, value):
    for i in range(x, x + k + 1):
        for j in range(y, y + k + 1):
            board[i][j] = value

def backtracking(count):
    global result
    if result < count: return
    if is_fill_with_value(0, 0, 9, 0):
        result = min(result, count)
        return

    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                for k in reversed(range(5)):
                    if paper[k] > 0 and not out_of_bound(i + k, j + k) and is_fill_with_value(i, j, k, 1):
                        paper[k] -= 1
                        fill(i, j, k, 0)
                        backtracking(count + 1)
                        fill(i, j, k, 1)
                        paper[k] += 1
                return

board = []
paper = [5 for _ in range(5)]
result = 100
board = [(list(map(int, input().split()))) for _ in range(10)]
backtracking(0)
print(-1 if result == 100 else result)