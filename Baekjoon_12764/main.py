import sys
input = sys.stdin.readline
MAX = 100000

n = int(input())
arr = []
for _ in range(n):
    p, q = map(int, input().split())
    arr.append((p, q))
arr.sort()

closed = [0 for _ in range(MAX + 1)]
count = [0 for _ in range(MAX + 1)]
for (start, end) in arr:
    for idx, each_computer in enumerate(closed):
        if each_computer <= start:
            closed[idx] = end
            count[idx] += 1
            break

result = 0
for each in count:
    if not each: break
    result += 1
print(result)
print(*count[:result])