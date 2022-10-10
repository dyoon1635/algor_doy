import sys

n, m = map(int, sys.stdin.readline().split())
num = [i for i in range(n + 1)]

def union(a, b):
    x, y = find(a), find(b)
    if x != y:
        num[y] = x

def find(x):
    if num[x] == x: return x
    num[x] = find(num[x])
    return num[x]
    #return find(num[x])

for _ in range(m):
    x, a, b = map(int, sys.stdin.readline().split())
    print(*num)
    if x == 0: union(a, b)
    elif x == 1:
        if find(a) == find(b): print('YES')
        else: print('NO')