import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

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
    tmp.append(node)

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
re_adj = [[] for _ in range(n + 1)]
for _ in range(m):
    v, w = map(int, input().split())
    adj[v].append(w)
    re_adj[w].append(v)

visited = [False for _ in range(n + 1)]
stack = []
for cur_node in range(1, n + 1):
    if not visited[cur_node]: dfs(cur_node)

visited = [False for _ in range(n + 1)]
scc = []
scc_num = [-1 for _ in range(n + 1)]
scc_idx = -1
while stack:
    cur_node = stack.pop()
    if not visited[cur_node]:
        tmp = []
        scc_idx += 1
        re_dfs(cur_node)
        scc.append(tmp)
scc_indegree = [0 for _ in range(len(scc))]

for each_node in range(1, n + 1):
    for next in adj[each_node]:
        if scc_num[each_node] != scc_num[next]:
            scc_indegree[scc_num[next]] += 1

if len(scc) == 1: print('Yes')
else:
    cnt = 0
    for each in scc_indegree:
        if each == 0: cnt += 1
    print('Yes' if cnt == 0 else 'No')