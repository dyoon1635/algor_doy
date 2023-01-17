import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(x):
    if x == parent[x]: return parent[x]
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    if x < y: parent[b] = a
    else: parent[a] = b

n, p = map(int, input().split())
parent = [i for i in range(n + 1)]
cost = [0]
for _ in range(n):
    cost.append(int(input()))

bridge = []
for _ in range(p):
    s, e, l = map(int, input().split())
    bridge.append((2 * l + cost[s] +  cost[e], s, e))
    #bridge.append((l + cost[s], e, s))
bridge.sort()

result = 0
for l, s, e in bridge:
    if find(s) != find(e):
        union(s, e)
        #print(s, e)
        result += l
print(result + min(cost[1:]))
