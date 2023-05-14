import sys
from collections import deque
input = sys.stdin.readline

def get_depth():
    dq = deque()
    for idx, each_p in enumerate(parent):
        if idx == each_p:
            dq.append((idx, 0)) # node, depth
            visited[idx] = True
    while dq:
        node, d = dq.popleft()
        for next in adj[node]:
            if not visited[next]:
                dq.append((next, d + 1))
                depth[next] = d + 1
                visited[next] = True

def LCA(a, b):
    if depth[a] < depth[b]: a, b = b, a
    while depth[a] != depth[b]:
        a = parent[a]
    while a != b:
        a, b = parent[a], parent[b]
    return a

for _ in range(int(input())):
    n = int(input())
    adj = [[] for _ in range(n + 1)]
    depth = [0 for _ in range(n + 1)]
    parent = [i for i in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        parent[b] = a
    node_a, node_b = map(int, input().split())
    get_depth()
    print(LCA(node_a, node_b))
