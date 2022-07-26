sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input())))

def get_idx(n):
    return (n // 9, n % 9)

def row_check(num, x):
    if num in sudoku[x]: return False
    return True

def col_check(num, y):
    for row in sudoku:
        if row[y] == num: return False
    return True

def box_check(num, x, y):
    row_box, col_box = 3 * (x // 3), 3 * (y // 3)
    for row in range(row_box, row_box + 3):
        for col in range(col_box, col_box + 3):
            if sudoku[row][col] == num: return False
    return True

def possible(num, idx):
    x, y = get_idx(idx)
    return (row_check(num, x) and \
            col_check(num, y) and \
            box_check(num, x, y))

def printf():
    for row in sudoku:
        for num in row:
            print(num, end='')
        print('')

def dfs(idx):
    global sudoku

    x, y = 0, 0
    while True:
        x, y = get_idx(idx)
        if idx > 80:
            printf()
            exit(0)
        if sudoku[x][y] == 0: break
        idx += 1

    for num in range(1, 10):
        if possible(num, idx):
            sudoku[x][y] = num
            dfs(idx + 1)
            sudoku[x][y] = 0

if __name__ == "__main__":
    dfs(0)
    """dq = deque()
    dq.appendleft([sudoku, 0])

    while dq:
        sol, idx = dq.popleft()

        while True:
            x, y = get_idx(idx)
            if idx > 80:
                printf(sol)
                exit(0)

            if sol[x][y] == 0:
                break
            idx += 1

        for num in reversed(range(1, 10)):
            if possible(sol, num, idx):
                x, y = get_idx(idx)
                tmp = copy.deepcopy(sol)
                tmp[x][y] = num
                dq.appendleft([tmp, idx])
"""