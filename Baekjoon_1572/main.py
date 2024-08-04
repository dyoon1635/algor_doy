import sys, math
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 65537
leaf = [int(input()) for _ in range(n)]

class SegTree:
    def __init__(self):
        self.tree = [0 for _ in range(MAX * 4)]

    def update(self, start, end, idx, node, value):
        if start <= node <= end:
            self.tree[idx] += value
            if start == end:
                return

            mid = (start + end) // 2
            self.update(start, mid, idx * 2, node, value)
            self.update(mid + 1, end, idx * 2 + 1, node, value)

    def search(self, start, end, idx, value):
        if start == end:
            return start

        mid = (start + end) // 2
        left = self.tree[idx * 2]
        if left >= value:
            return self.search(start, mid, idx * 2, value)
        return self.search(mid + 1, end, idx * 2 + 1, value - left)

segtree = SegTree()
result = 0
for i in range(n):
    segtree.update(0, MAX, 1, leaf[i], 1)
    if i > k - 1:
        segtree.update(0, MAX, 1, leaf[i - k], -1)
    if i >= k - 1:
        result += segtree.search(0, MAX, 1, (k + 1) // 2)
print(result)
