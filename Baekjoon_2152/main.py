import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    for next in Graph[node]:
        if not visited[next]: dfs(next)
    stack.append(node)

def re_dfs(node):
    visited[node] = True
    for next in reGraph[node]:
        if not visited[next]: re_dfs(next)
    tmp.append(node)
    scc_idx[node] = idx

n, m ,s, t = map(int, input().split())
Graph, reGraph = [[] for _ in range(n + 1)], [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    Graph[a].append(b)
    reGraph[b].append(a)

stack, scc = [], []
visited = [False for _ in range(n + 1)]
for i in range(1, n + 1):
    if not visited[i]: dfs(i)

scc_idx = [-1 for _ in range(n + 1)]; idx = -1
visited = [False for _ in range(n + 1)]
while stack:
    node = stack.pop()
    tmp = []
    if not visited[node]:
        idx += 1
        re_dfs(node)
        scc.append(len(tmp))

scc_adj = [[] for _ in range(len(scc))]
for node in range(1, n + 1):
    for next in Graph[node]:
        if scc_idx[node] != scc_idx[next] and \
                scc_idx[next] not in scc_adj[scc_idx[node]]:
            scc_adj[scc_idx[node]].append(scc_idx[next])

if scc_idx[s] == scc_idx[t]: print(scc[scc_idx[s]])
else:
    dist = [0 for _ in range(len(scc))]; dist[scc_idx[s]] = scc[scc_idx[s]]
    q = deque()
    q.append((scc_idx[s], dist[scc_idx[s]]))
    while q:
        scc_num, cost = q.popleft()
        for next_scc in scc_adj[scc_num]:
            new_cost = cost + scc[next_scc]
            if dist[next_scc] < new_cost:
                dist[next_scc] = new_cost
                q.append((next_scc, new_cost))
    print(dist[scc_idx[t]])