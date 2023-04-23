import sys
from math import *
input = sys.stdin.readline

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

n = int(input())
pos = [list(map(int, input().split())) for _ in range(n)]

minDist = sys.maxsize
x, y = 0, 0
for x1, y1 in pos:
    maxDist = 0
    for x2, y2 in pos:
        if x1 == x2 and y1 == y2: continue
        maxDist = max(maxDist, distance(x1, y1, x2, y2))
    if maxDist < minDist:
        minDist = maxDist
        x, y = x1, y1
print(x, y)