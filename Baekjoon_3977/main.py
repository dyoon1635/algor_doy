import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(node):
    visited[node] = True
    for each in adj[node]:
        if not visited[each]:
            dfs(each)
    stack.append(node)

def re_dfs(node):
    visited[node] = True
    for each in re_adj[node]:
        if not visited[each]:
            re_dfs(each)
    each_scc.append(node)

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    adj, re_adj = [[] for _ in range(n)], [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        re_adj[v].append(u)

    stack = []
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]: dfs(i)

    scc = []
    scc_idx = -1
    visited = [False for _ in range(n)]
    scc_group = [-1 for _ in range(n)]
    for each in reversed(stack):
        if not visited[each]:
            scc_idx += 1
            each_scc = []
            re_dfs(each)
            scc.append(each_scc)
            for each in each_scc:
                scc_group[each] = scc_idx

    scc_indegree = [0 for _ in range(scc_idx + 1)]
    for i in range(n):
        for each in adj[i]:
            if scc_group[i] != scc_group[each]:
                scc_indegree[scc_group[each]] += 1
    result = []
    count = 0
    for i, each in enumerate(scc_indegree):
        if not each:
            count += 1
            for node in scc[i]:
                result.append(node)
    if count == 1:
        result.sort()
        for each in result:
            print(each)
    else: print('Confused')
    input(); print('')