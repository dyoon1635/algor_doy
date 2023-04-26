import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def find(x):
    if x == parent[x]: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px, py = find(x), find(y)
    parent[max(px, py)] = min(px, py)

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
k, *people = map(int, input().split())
for each in people:
    union(0, each)

count = 0
parties = []
for _ in range(m):
    num, *party = map(int, input().split())
    parties.append(party)
    for i in range(num - 1):
        pa, pb = find(party[i]), find(party[i + 1])
        if pa != pb: union(pa, pb)
for each_party in parties:
    if find(each_party[0]) != 0:
        count += 1
print(count)