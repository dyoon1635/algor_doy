import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    for next in adj[node]:
        if not visited[next]: dfs(next)
    stack.append(node)

def re_dfs(node):
    visited[node] = True
    scc_num[node] = scc_idx
    for next in re_adj[node]:
        if not visited[next]: re_dfs(next)
    tmp_scc.append(node)

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
re_adj = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    re_adj[y].append(x)

stack = []
visited = [False for _ in range(n + 1)]
for node in range(1, n + 1):
    if not visited[node]: dfs(node)

scc = []
scc_idx = -1
scc_num = [-1 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
while stack:
    node = stack.pop()
    if not visited[node]:
        tmp_scc = []
        scc_idx += 1
        re_dfs(node)
        scc.append(tmp_scc)

scc_indegree = [0 for _ in range(len(scc))]
for node in range(1, n + 1):
    for next in adj[node]:
        if scc_num[node] != scc_num[next]:
            scc_indegree[scc_num[next]] += 1

count = 0
for each in scc_indegree:
    if each == 0: count += 1
print(count)