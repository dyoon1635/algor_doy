import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    for next in adj[node]:
        if not visited[next]:
            dfs(next)
    stack.append(node)

def re_dfs(node):
    visited[node] = True
    for next in re_adj[node]:
        if not visited[next]:
            re_dfs(next)
    scc_num[node] = scc_idx
    each_component.append(node)

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
re_adj = [[] for _ in range(n + 1)]
for _ in range(m):
    v, w = map(int, input().split())
    adj[v].append(w)
    re_adj[w].append(v)

stack = []
visited = [False for _ in range(n + 1)]
for each_node in range(1, n + 1):
    if not visited[each_node]: dfs(each_node)

scc = []
visited = [False for _ in range(n + 1)]
scc_num = [-1 for _ in range(n + 1)]
scc_idx = -1
while stack:
    each_node = stack.pop()
    if not visited[each_node]:
        scc_idx += 1
        each_component = []
        re_dfs(each_node)
        scc.append(each_component)

scc_adj = [[] for _ in range(len(scc))]
scc_indegree = [0 for _ in range(len(scc))]
for each_node in range(1, n + 1):
    cur_scc = scc_num[each_node]
    for next_node in adj[each_node]:
        next_scc = scc_num[next_node]
        if cur_scc != next_scc:
            scc_indegree[next_scc] += 1
            scc_adj[cur_scc].append(next_scc)

stack, topology = [], []
for idx, indegree in enumerate(scc_indegree):
    if indegree == 0: stack.append(idx)

while stack:
    if len(stack) > 1: break
    cur_scc = stack.pop(0)
    topology.append(cur_scc)
    for next_scc in scc_adj[cur_scc]:
        scc_indegree[next_scc] -= 1
        if scc_indegree[next_scc] == 0: stack.append(next_scc)
if len(topology) == len(scc):
    print(len(scc[topology[0]]))
    for each in sorted(scc[topology[0]]): print(each, end=' ')
    exit(0)
print(0)
