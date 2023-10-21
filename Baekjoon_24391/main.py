import sys, heapq
input = sys.stdin.readline

def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    parent[max(px, py)] = min(px, py)

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    union(i, j)

lecture = list(map(int, input().split()))
answer = 0
for i in range(n - 1):
    if find(lecture[i]) != find(lecture[i + 1]): answer += 1
print(answer)