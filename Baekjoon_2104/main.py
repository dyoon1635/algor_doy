import sys, math
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = ((leaf[start], start), leaf[start]) # min, idx, sum
    else:
        tree[node * 2] = init(node * 2, start, (start + end) // 2)
        tree[node * 2 + 1] = init(node * 2 + 1, (start + end) // 2 + 1, end)
        tree[node] = (min(tree[node * 2][0], tree[node * 2 + 1][0]),
                      tree[node * 2][1] + tree[node * 2 + 1][1])
    return tree[node]

def query(node, start, end, left, right):
    if start > right or end < left: return ((sys.maxsize, sys.maxsize), 0)
    if left <= start and end <= right: return tree[node]

    mid = (start + end) // 2
    left_sub_tree = query(node * 2, start, mid, left, right)
    right_sub_tree = query(node * 2 + 1, mid + 1, end, left, right)
    return (min(left_sub_tree[0], right_sub_tree[0]),
            left_sub_tree[1] + right_sub_tree[1])

def solve(left, right):
    if left == right: return leaf[left] ** 2
    if left > right: return -1

    (min_val, idx), sub_sum = query(1, 0, n - 1, left, right)
    return max(min_val * sub_sum,
               solve(left, idx - 1),
               solve(idx + 1, right))

n = int(input())
leaf = list(map(int, input().split()))
tree = [(sys.maxsize, 0) for _ in range(2 ** (math.ceil(math.log(n, 2)) + 1))] # min, sum
init(1, 0, n - 1)
print(solve(0, n - 1))
