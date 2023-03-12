import sys
input = sys.stdin.readline

n = int(input())
coord = []
for _ in range(n):
    coord.append(list(map(int, input().split())))
coord.sort(reverse=True)

ymax = coord[0][1]
S = coord[0][0] * coord[0][1]
for x, y in coord:
    if ymax >= y: continue
    S += (x * (y - ymax))
    ymax = y
print(S)