import sys, math
input = sys.stdin.readline

class SegTree:
    def __init__(self):
        self.tree_size = 2 ** (math.ceil(math.log2(n)) + 1)
        self.tree = [0 for _ in range(self.tree_size)]
        self.lazy = [0 for _ in range(self.tree_size)]
        self.init_tree(0, self.tree_size, 1)

    def init_tree(self, start, end, node):
        if not (start <= node <= end):
            return 0
        if start == end:
            self.tree[start] = leaf[node]
            return self.tree[start]
        mid = (start + end) // 2
        self.tree[node] = self.init_tree(start, mid, node * 2) + \
                          self.init_tree(mid + 1, end, node * 2 + 1)
        return self.tree[node]

    def updateLazy(self, start, end, node):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

    def updateRange(self, start, end, node, left, right, value):
        self.updateLazy(start, end, node)
        if start > right or end < start:
            return
        if left <= start and end <= right:
            self.lazy[node] += value
            self.updateLazy(start, end, node)
            return
        mid = (start + end) // 2
        self.updateRange(start, mid, node * 2, left, right, value)
        self.updateRange(mid + 1, end, node * 2 + 1, left, right, value)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def subSum(self, start, end, node, left, right):
        self.updateLazy(start, end, node)
        if start > right or end < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self.subSum(start, mid, node * 2, left, right) + \
               self.subSum(mid + 1, end, node * 2 + 1, left, right)


n, m, k = map(int, input().split())
leaf = [int(input()) for _ in range(n)]
segtree = SegTree()
MAX = segtree.tree_size
for _ in range(m + k):
    op, *cmd = map(int, input().split())
    if op == 1:
        start, end, value = cmd
        segtree.updateRange(0, MAX, 1, start, end, value)
    else:
        start, end = cmd
        segtree.subSum(0, MAX, 1, start, end)