import sys
input = sys.stdin.readline

def count_acorn(box):
    count = 0
    for start, end, c in rules:
        if box < start: continue
        end = min(end, box)
        count += (end - start) // c + 1
    return count

def binarySearch():
    start, end = 0, n
    while start < end:
        mid = (start + end) // 2
        tmp_count = count_acorn(mid)

        if tmp_count < d: start = mid + 1
        else: end = mid
    return start

n, k, d = map(int, input().split())
rules = [list(map(int, input().split())) for _ in range(k)]
print(binarySearch())