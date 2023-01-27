import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(node):
    visited[node] = True
    for each in adj[node]:
        if not visited[each]: dfs(each)
    stack.append(node)

def re_dfs(node):
    visited[node] = True
    for each in re_adj[node]:
        if not visited[each]: re_dfs(each)
    each_scc.append(node)

n = int(input())
cost = [0] + list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]
re_adj = [[] for _ in range(n + 1)]
for idx in range(1, n + 1):
    tmp = list(map(int, input().strip()))
    for i in range(n):
        if tmp[i]:
            adj[idx].append(i + 1)
            re_adj[i + 1].append(idx)

stack = []
visited = [False for _ in range(n + 1)]
for each in range(1, n + 1):
    if not visited[each]: dfs(each)

scc = []
visited = [False for _ in range(n + 1)]
for each in reversed(stack):
    if not visited[each]:
        each_scc = []
        re_dfs(each)
        scc.append(each_scc)

totalCost = 0
for each_scc in scc:
    each_cost = sys.maxsize
    for each in each_scc:
        each_cost = min(each_cost, cost[each])
    totalCost += each_cost
print(totalCost)