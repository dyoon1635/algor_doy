import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    if a != b: parent[x] = y

n, q = map(int, input().split())
parent = [i for i in range(n + 1)]
pnode = [i for i in range(n + 1)]
for i in range(1, n):
    pnode[i + 1] = int(input())

query = deque()
for _ in range(n - 1 + q):
    query.append(list(map(int, input().split())))

answer = []
while query:
    each_query = query.pop()
    if not each_query[0]: # if zero
        b = each_query[1]
        union(b, pnode[b])
    else:
        c, d = each_query[1:]
        answer.append(find(c) == find(d))

for each in reversed(answer):
    print('YES' if each else 'NO')