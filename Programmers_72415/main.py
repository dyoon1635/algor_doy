from itertools import permutations
from collections import deque
import sys

def out_of_bound(x, y):
    if x < 0 or x >= 4 or y < 0 or y >= 4: return True
    return False

def move_count(x1, y1, x2, y2, board):
    if x1 == x2 and y1 == y2: return 0
    dq = deque()
    visited = [[False] * 4 for _ in range(4)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited[x1][y1] = True
    dq.append([x1, y1, 0])
    while dq:
        x, y, cnt = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] # 1칸 이동
            if out_of_bound(nx, ny): continue
            if nx == x2 and ny == y2: return cnt + 1
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dq.append([nx, ny, cnt + 1])
            if board[nx][ny]: continue

            while True:
                nx, ny = nx + dx[i], ny + dy[i]
                if nx == x2 and ny == y2: return cnt + 1
                if out_of_bound(nx, ny):
                    visited[nx - dx[i]][ny - dy[i]] = True
                    dq.append([nx - dx[i], ny - dy[i], cnt + 1])
                    break
                if board[nx][ny]:
                    visited[nx][ny] = True
                    dq.append([nx, ny, cnt + 1])
                    break

def get_distance(board, each, pair, r, c):
    # each : 제거할 카드 순서 [3, 1, 4] -> 3번 card, 1번 card, 4번 card순
    # pair : 해당 카드의 위치 x1, y1, x2, y2
    tmp = None
    for i in range(4):
        tmp = [board[i][:] for i in range(4)]
    res = sys.maxsize
    dq = deque()
    dq.append([r, c, 0, 0])  # 현재 위치, 제거할 카드의 idx, distance
    while dq:
        x, y, idx, dist = dq.popleft()
        if idx >= len(each):
            res = min(res, dist)
            continue
        (x1, y1), (x2, y2) = pair[each[idx]]

        # case1 : (x1, y1) -> (x2, y2)
        diff = move_count(x, y, x1, y1, tmp) + move_count(x1, y1, x2, y2, tmp)
        #print('({}, {}) -> ({}, {}) -> ({}, {}) : {} and {}'.format(x, y, x1, y1, x2, y2, move_count(x, y, x1, y1, tmp), move_count(x1, y1, x2, y2, tmp)))
        dq.append([x2, y2, idx + 1, dist + diff])

        # case2 : (x2, y2) -> (x1, y1)
        diff = move_count(x, y, x2, y2, tmp) + move_count(x2, y2, x1, y1, tmp)
        #print('({}, {}) -> ({}, {}) -> ({}, {}) : {} and {}'.format(x, y, x2, y2, x1, y1, move_count(x, y, x2, y2, tmp), move_count(x2, y2, x1, y1, tmp)))
        tmp[x1][y1], tmp[x2][y2] = 0, 0
        dq.append([x1, y1, idx + 1, dist + diff])
    return res

def solution(board, r, c):
    pair = [[] for _ in range(7)] # 지워야 할 카드의 위치쌍
    card = [] # 지워야 할 card
    answer = sys.maxsize
    for x, row in enumerate(board):
        for y, each in enumerate(row):
            if each: # if not zero
                pair[each].append([x, y])
                if each not in card: card.append(each)
    case = permutations(card)
    for each in case:
        answer = min(answer, get_distance(board, each, pair, r, c))
    return answer + (len(card) * 2) # move count + enter