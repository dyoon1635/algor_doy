import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
N = n ** 2
classroom = [[0] * n for _ in range(n)]
prefered = [[0] * (N + 1) for _ in range(N + 1)]
student_info = deque()

for i in range(N):
    stu_data = list(map(int, sys.stdin.readline().split()))
    student_info.append(stu_data)
    for i in range(1, len(stu_data)):
        prefered[stu_data[0]][stu_data[i]] = 1


def out_of_bound(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return True
    return False

def find_seat(stu_data):
    stu, prefer_stu = stu_data[0], stu_data[1:]
    possible = [] # 좋아하는 학생 수, 비어있는 칸 수, 좌표

    for x in range(n):
        for y in range(n):
            prefer_cnt, empty_cnt = 0, 0
            if not classroom[x][y]:
                for dir in range(4):
                    nx, ny = x + dx[dir], y + dy[dir]
                    if not out_of_bound(nx, ny):
                        if classroom[nx][ny] in prefer_stu:
                            prefer_cnt += 1
                        if not classroom[nx][ny]:
                            empty_cnt += 1
                possible.append([-prefer_cnt, -empty_cnt, [x, y]])
    possible.sort()
    return possible[0][2]

def find_preference():
    total = 0
    for x in range(n):
        for y in range(n):
            cnt = 0
            cur_stu = classroom[x][y]
            for dir in range(4):
                nx, ny = x + dx[dir], y + dy[dir]
                if not out_of_bound(nx, ny):
                    next_stu = classroom[nx][ny]
                    if prefered[cur_stu][next_stu]: cnt += 1

            if cnt != 0:
                total += (10 ** (cnt - 1))
    return total


first = student_info.popleft()
classroom[1][1] = first[0]
while student_info:
    stu_data = student_info.popleft()
    x, y = find_seat(stu_data)
    classroom[x][y] = stu_data[0]
print(find_preference())