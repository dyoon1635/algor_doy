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
    global cost
    visited[node] = True
    scc_idx[node] = idx
    for next in reGraph[node]:
        if scc_idx[next] == -1: re_dfs(next)
        elif scc_idx[node] != scc_idx[next]:
            scc_adj[scc_idx[next]].append(scc_idx[node])
    cost += ATM[node]

n, m = map(int, input().split())
Graph, reGraph = [[] for _ in range(n + 1)], [[] for _ in range(n + 1)]
ATM = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    Graph[a].append(b)
    reGraph[b].append(a)

for i in range(1, n + 1):
    ATM[i] = int(input())

s, p = map(int, input().split())
restaurant = list(map(int, input().split()))

stack, scc = [], []
scc_idx = [-1 for _ in range(n + 1)]; idx = -1
scc_adj = []
visited = [False for _ in range(n + 1)]
for i in range(1, n + 1):
    if not visited[i]: dfs(i)

while stack:
    node = stack.pop()
    cost = 0
    if scc_idx[node] == -1:
        scc_adj.append([])
        idx += 1
        re_dfs(node)
        scc.append(cost)

del Graph, reGraph, visited

dist = [0 for _ in range(len(scc))]
dist[scc_idx[s]] = scc[scc_idx[s]]
q = deque([scc_idx[s]]) #q.append((scc_idx[s], dist[scc_idx[s]]))
while q:
    cur_scc = q.popleft()
    for next_scc in scc_adj[cur_scc]:
        if dist[cur_scc] + scc[next_scc] > dist[next_scc]:
            dist[next_scc] = dist[cur_scc] + scc[next_scc]
            q.append(next_scc)
answer = 0
for each in restaurant:
    idx = scc_idx[each]
    answer = max(answer, dist[idx])
print(answer)