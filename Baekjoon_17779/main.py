from itertools import combinations_with_replacement, permutations
import sys

n = int(sys.stdin.readline())
area = []
area.append([0] * (n + 1))
for _ in range(n):
    area.append([0] + list(map(int, sys.stdin.readline().split())))

def split_area(x, y, d1, d2):
    boundary = [[0] * (n + 1) for _ in range(n + 1)]
    boundary[x][y] = 1
    for i in range(1, d1 + 1):
        boundary[x + i][y - i] = 1
        boundary[x + d2 + i][y + d2 - i] = 1
    for i in range(1, d2 + 1):
        boundary[x + i][y + i] = 1
        boundary[x + d1 + i][y - d1 + i] = 1

    total = 0
    for each in area: total += sum(each)
    area_size = [0, 0, 0, 0]
    # 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if boundary[r][c]: break
            area_size[0] += area[r][c]
    # 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
    for r in range(1, x + d2 + 1):
        for c in range(n, y, -1):
            if boundary[r][c]: break
            area_size[1] += area[r][c]
    # 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    for r in range(x + d1, n + 1):
        for c in range(1, y - d1 + d2):
            if boundary[r][c]: break
            area_size[2] += area[r][c]
    # 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
    for r in range(x + d2 + 1, n + 1):
        for c in range(n, y - d1 + d2 - 1, -1):
            if boundary[r][c]: break
            area_size[3] += area[r][c]
    area_size.append(total - sum(area_size))
    return max(area_size) - min(area_size)

all_case = combinations_with_replacement([i for i in range(1, n + 1)], 4)
res = sys.maxsize
for each_case in all_case:
    tmp = permutations(each_case)
    for x, y, d1, d2 in tmp:
        # d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N,
        # 1 ≤ y-d1 < y < y+d2 ≤ N
        if x + d1 + d2 > n or y - d1 < 1 or y + d2 > n: continue
        res = min(res, split_area(x, y, d1, d2))
print(res)
