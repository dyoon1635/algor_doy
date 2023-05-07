import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def init(node, level):
    visited[node] = True
    for next in adj[node]:
        if not visited[next]:
            depth[next] = level + 1
            parent[next] = node
            init(next, level + 1)

def LCA(x, y):
    while depth[x] != depth[y]:
        if depth[x] > depth[y]: x = parent[x]
        else: y = parent[y]

    while x != y:
        x, y = parent[x], parent[y]
    return x

n = int(input())
depth = [0 for _ in range(n + 1)]
parent = [i for i in range(n + 1)]
visited = [False for _ in range(n + 1)]
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

init(1, 0)
for _ in range(int(input())):
    s, e = map(int, input().split())
    print(LCA(s, e))