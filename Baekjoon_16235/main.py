from collections import deque
import sys

n, m, k = map(int, input().split())
A = []
field = [[5] * n for _ in range(n)]
forest = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    forest[x - 1][y - 1].append(z)

def out_of_bound(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return True
    return False

def printf():
    for i in range(n):
        for j in range(n):
            print(i, j, '> : ', end=' ')
            print(forest[i][j])

def spring():
    for i in range(n):
        for j in range(n):
            if forest[i][j]:
                for idx, age in enumerate(forest[i][j]):
                    if age <= field[i][j]:
                        field[i][j] -= age
                        forest[i][j][idx] += 1
                    else:
                        forest[i][j][idx] *= (-1)

def summer():
    for i in range(n):
        for j in range(n):
            while forest[i][j]:
                dead_tree = forest[i][j][-1]
                if dead_tree > 0: break

                field[i][j] += int((-dead_tree) / 2)
                forest[i][j].pop()

def autumn():
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(n):
        for j in range(n):
            if forest[i][j]:
                for age in forest[i][j]:
                    if age % 5 == 0:
                        for k in range(8):
                            nx, ny = i + dx[k], j + dy[k]
                            if not out_of_bound(nx, ny):
                                forest[nx][ny].appendleft(1)

def winter():
    for i in range(n):
        for j in range(n):
            field[i][j] += A[i][j]

def count():
    res = 0
    for i in range(n):
        for j in range(n):
            res += len(forest[i][j])
    return res

if __name__ == "__main__":
    for _ in range(k):
        spring()
        summer()
        autumn()
        winter()
    print(count())

