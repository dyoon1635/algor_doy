import sys
input = sys.stdin.readline

def get_len(a, b): # a, b구간의 길이
    length = 0
    for (x, y) in arr:
        if b <= x: break
        left, right = max(x, a), min(y, b)
        length += (right - left)
    return length

n, k = map(int, input().split())
arr = []
M = 0
for _ in range(n):
    x, y = map(int, input().split())
    M = max(M, y)
    arr.append((x, y))
arr.sort()

lp, rp = 0, 0
while lp <= rp and rp <= M:
    l = get_len(lp, rp)
    if l == k:
        print(lp, rp)
        exit(0)
    if l < k: rp += 1
    else: lp += 1
print(0, 0)
