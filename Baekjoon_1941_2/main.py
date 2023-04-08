from itertools import combinations
from collections import deque

def out_of_bound(x, y):
    return not (0 <= x < 5 and 0 <= y < 5)

def get_pos(num):
    return (num // 5, num % 5)

def y_count(each_case):
    count = 0
    for each in each_case:
        x, y = get_pos(each)
        if classroom[x][y] == 'Y': count += 1
        if count > 3: return False
    return True

def is_connected(each_case):
    check_board = [[False] * 5 for _ in range(5)]
    visited = [[False] * 5 for _ in range(5)]
    count = 0
    for each in each_case:
        x, y = get_pos(each)
        check_board[x][y] = True

    for i in range(5):
        for j in range(5):
            if check_board[i][j] and not visited[i][j]:
                count += 1
                if count > 1: return False
                dq = deque()
                dq.append((i, j))
                visited[i][j] = True
                while dq:
                    cx, cy = dq.popleft()
                    for dir in range(4):
                        nx, ny = cx + dx[dir], cy + dy[dir]
                        if not out_of_bound(nx, ny) and not visited[nx][ny] and check_board[nx][ny]:
                            visited[nx][ny] = True
                            dq.append((nx, ny))
    return True if count == 1 else False

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
classroom = []
for _ in range(5):
    classroom.append(list(input().strip()))

result = 0
all_case = combinations([i for i in range(25)], 7)
for each in all_case:
    if not y_count(each) or not is_connected(each): continue
    result += 1
print(result)