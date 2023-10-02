def row_check(r, new_num):
    for i in range(9):
        if sudoku[r][i] == new_num: return False
    return True

def col_check(c, new_num):
    for i in range(9):
        if sudoku[i][c] == new_num: return False
    return True

def square_check(r, c, new_num):
    r, c = (r // 3) * 3, (c // 3) * 3
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            if sudoku[i][j] == new_num: return False
    return True

def backtracking(idx):
    if idx == n:
        for each in sudoku:
            print(*each)
        exit(0)

    r, c = blank[idx]
    for num in range(1, 10):
        if row_check(r, num) and col_check(c, num) and square_check(r, c, num):
            sudoku[r][c] = num
            backtracking(idx + 1)
            sudoku[r][c] = 0

sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0: blank.append((i, j))
n = len(blank)
backtracking(0)