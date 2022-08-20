import sys
r, c = map(int, input().split())
if r % 2 != 0:
    print((('R' * (c - 1) + 'D') + ('L' * (c - 1) + 'D')) * (r // 2) + 'R' * (c - 1))
elif c % 2 != 0:
    print((('D' * (r - 1) + 'R') + ('U' * (r - 1) + 'R')) * (c // 2) + 'D' * (r - 1))
else:
    board = []
    for _ in range(r):
        board.append(list(map(int, sys.stdin.readline().split())))

    ex, ey, val = -1, -1, 1000
    for i in range(0, r, 2):
        for j in range(1, c, 2):
            if val > board[i][j]: ex, ey, val = i, j, board[i][j]
    for i in range(1, r, 2):
        for j in range(0, c, 2):
            if val > board[i][j]: ex, ey, val = i, j, board[i][j]

    result = (('D' * (r - 1) + 'R') + ('U' * (r - 1) + 'R')) * (ey // 2)
    cx, cy = 0, 2 * (ey // 2)
    yrange = [2 * (ey // 2), 2 * (ey // 2) + 1]
    while True:
        if cx == r - 1 and cy == yrange[1]: break
        #print(result, yrange, cx, cy)
        if cy + 1 == yrange[1] and [cx, cy + 1] != [ex, ey]:
            result += 'R'
            cy += 1
        elif cy - 1 == yrange[0] and [cx, cy - 1] != [ex, ey]:
            result += 'L'
            cy -= 1

        if cx != r - 1:
            result += 'D'
            cx += 1

    result += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - ey - 1) // 2)
    print(result)