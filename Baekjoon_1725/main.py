import sys, math
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = (leaf[start], start)
    else:
        mid = (start + end) // 2
        tree[node] = min(init(node * 2, start, mid),
                         init(node * 2 + 1, mid + 1, end))
    return tree[node]

def sub_query(node, start, end, left, right):
    if start > right or end < left: return (sys.maxsize, sys.maxsize)
    if left <= start and end <= right: return tree[node]
    mid = (start + end) // 2
    return min(sub_query(node * 2, start, mid, left, right),
               sub_query(node * 2 + 1, mid + 1, end, left, right))

def solve(left, right):
    if left == right: return leaf[left]
    if left > right: return -1

    min_val, idx = sub_query(1, 0, n - 1, left, right)
    #print(min_val, idx)
    return max(min_val * (right - left + 1),
               solve(left, idx - 1),
               solve(idx + 1, right))

while True:
    n, *leaf = map(int, input().split())
    if n == 0: break
    #n = int(input())
    #leaf = [int(input()) for _ in range(n)]
    tree = [(0, 0) for _ in range(2 ** (math.ceil(math.log(n, 2))+1))]
    init(1, 0, n - 1)
    print(solve(0, n - 1))