import sys, heapq
from math import *
input = sys.stdin.readline

def get_distance(x1, y1, x2, y2):
    return sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        parent[max(px, py)] = min(px, py)

n = int(input())
stars = []
parent = [i for i in range(n)]
visited = [False for _ in range(n)]
pq = []
for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

for i in range(n):
    for j in range(n):
        if i == j: continue
        (x1, y1), (x2, y2) = stars[i], stars[j]
        distance = round(get_distance(x1, y1, x2, y2), 2)
        heapq.heappush(pq, (distance, i, j))

result = 0
while pq:
    distance, x, y = heapq.heappop(pq)
    if find(x) != find(y):
        union(x, y)
        result += distance
print(result)