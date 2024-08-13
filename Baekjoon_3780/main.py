import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def find(x):
    if x == parent[x]:
        return x
    #parent[x] = find(parent[x])
    tmp = find(parent[x])
    distance[x] += distance[parent[x]]
    parent[x] = tmp
    return parent[x]

def union(x, y):
    distance[x] = abs(x - y) % 1000
    parent[x] = y

for _ in range(int(input())):
    n = int(input())

    distance = [0 for _ in range(n + 1)]
    parent = [i for i in range(n + 1)]

    while True:
        op, *tmp = input().split()
        if op == 'O':
            break
        elif op == 'E':
            x = int(tmp[0])
            find(x)
            print(distance[x])
        elif op == 'I':
            x, y = map(int, tmp)
            union(x, y)
