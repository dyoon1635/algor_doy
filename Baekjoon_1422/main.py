from functools import cmp_to_key
import sys

def compare(x, y):
    X, Y = str(x), str(y)
    c1, c2 = X + Y, Y + X
    if c1 > c2: return -1
    return 1

k, n = map(int, sys.stdin.readline().split())
num = []
for _ in range(k):
    num.append(int(sys.stdin.readline().strip()))
num = num + [max(num)] * (n - k)
num.sort(key=cmp_to_key(compare))

for each in num:
    print(each, end='')