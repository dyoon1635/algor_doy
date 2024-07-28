import sys, bisect
from collections import deque
input = sys.stdin.readline

def out_of_bound(x, y):
    return not (0 <= x < n and 0 <= y < n)

def bfs(left, right):
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    dq = deque([(0, 0)])

    while dq:
        x, y = dq.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if not out_of_bound(nx, ny) and not visited[nx][ny] and left <= board[nx][ny] <= right:
                if nx == n - 1 and ny == n - 1:
                    return True
                visited[nx][ny] = True
                dq.append((nx, ny))
    return False

def solve(mid):
    start, end = board[0][0], board[-1][-1]
    for i in range(MIN, MAX + 1):
        if not (i <= start <= i + mid and i <= end <= i + mid):
            continue
        if bfs(i, i + mid):
            return True
    return False

def binary_search():
    left, right = 0, arr[-1]
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if solve(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    print(result)

if __name__ == "__main__":
    board = []
    arr = set()
    n = int(input())
    for _ in range(n):
        row = list(map(int, input().split()))
        for each in row:
            arr.add(each)
        board.append(row)
    arr = sorted(list(arr))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    MIN, MAX = arr[0], arr[-1]
    binary_search()