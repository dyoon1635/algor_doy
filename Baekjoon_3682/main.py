import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    for next in Graph[node]:
        if not visited[next]: dfs(next)
    stack.append(node)

def re_dfs(node):
    scc_idx[node] = idx
    for next in reGraph[node]:
        if scc_idx[next] == -1: re_dfs(next)
        elif scc_idx[node] != scc_idx[next]:
            scc_adj[scc_idx[next]].append(scc_idx[node])
            io_degree[scc_idx[node]][0] += 1
            io_degree[scc_idx[next]][1] += 1

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    Graph = [[] for _ in range(n + 1)]
    reGraph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s1, s2 = map(int, input().split())
        Graph[s1].append(s2)
        reGraph[s2].append(s1)

    stack = []
    visited = [False for _ in range(n + 1)]
    for node in range(1, n + 1):
        if not visited[node]: dfs(node)

    idx = -1
    scc_idx = [-1 for _ in range(n + 1)]
    scc, scc_adj = [], []
    io_degree = []
    while stack:
        node = stack.pop()
        if scc_idx[node] == -1:
            idx += 1
            io_degree.append([0, 0])
            scc_adj.append([])
            re_dfs(node)
    indegree, outdegree = 0, 0
    for IN, OUT in io_degree:
        if not IN: indegree += 1
        if not OUT: outdegree += 1
    if idx == 0: print(0)
    else: print(max(indegree, outdegree))