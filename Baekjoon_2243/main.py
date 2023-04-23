import sys
from math import *
input = sys.stdin.readline
N = 10 ** 6 + 1

def query(node, rank, start, end):
    if start == end: return start
    if rank <= tree[node * 2]:
        return query(node * 2, rank, start, (start + end) // 2)
    return query(node * 2 + 1, rank - tree[node * 2], (start + end) // 2 + 1, end)

def update(node, start, end, index, value):
    if index < start or index > end: return
    tree[node] += value
    if start != end:
        update(node * 2, start, (start + end) // 2, index, value)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, value)

n = int(input())
tree = [0 for _ in range(2 ** (ceil(log(N, 2)) + 1))]
for _ in range(n):
    a, *tmp = map(int, input().split())
    if a == 1:
        candy = query(1, tmp[0], 1, N)
        print(candy)
        update(1, 1, N, candy, -1)
    else:
        update(1, 1, N, tmp[0], tmp[1])