import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    for each in adj[node]:
        if not visited[each]: dfs(each)
    stack.append(node)

def re_dfs(node):
    visited[node] = True
    for each in re_adj[node]:
        if not visited[each]:
            re_dfs(each)
    each_scc.append(node)

n, m = map(int, input().split())
adj, re_adj = [[] for _ in range(n)], [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    re_adj[b].append(a)

stack = []
visited = [False for _ in range(n)]
for node in range(n):
    if not visited[node]:
        dfs(node)

scc = []
visited = [False for _ in range(n)]
scc_group = [-1 for _ in range(n)]; scc_idx = -1
for node in reversed(stack):
    if not visited[node]:
        scc_idx += 1
        each_scc = []
        re_dfs(node)
        scc.append(each_scc)

        for each in each_scc:
            scc_group[each] = scc_idx

scc_indegree = [0 for _ in range(scc_idx + 1)]
for node in range(n):
    for next in adj[node]:
        if scc_group[node] != scc_group[next]:
            scc_indegree[scc_group[next]] += 1

count = 0
for indegree in scc_indegree:
    if not indegree: count += 1
print(count)