import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(node):
    visited[node] = True
    for next in graph[node]:
        if not visited[next]:
            dfs(next)
    stack.append(node)

def re_dfs(node):
    visited[node] = True
    for next in re_graph[node]:
        if not visited[next]:
            re_dfs(next)
    scc.append(node)
    result.append(node)

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    graph, re_graph = [[] for _ in range(n + 1)], [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        re_graph[y].append(x)

    stack = []
    visited = [False for _ in range(n + 1)]
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    scc = []
    visited = [False for _ in range(n + 1)]
    scc_group = [-1 for _ in range(n + 1)]
    scc_idx, scc_num = 0, 0
    for each in reversed(stack):
        if not visited[each]:
            scc_num += 1
            result = []
            re_dfs(each)
            for node in result:
                scc_group[node] = scc_idx
            scc_idx += 1

    scc_indegree = [0 for _ in range(scc_num)]
    for i in range(1, n + 1):
        for next in graph[i]:
            if scc_group[i] != scc_group[next]:
                scc_indegree[scc_group[next]] += 1
    count = 0
    for each in scc_indegree:
        if each == 0: count += 1
    print(count)

