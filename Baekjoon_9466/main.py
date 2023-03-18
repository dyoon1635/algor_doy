import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
T = int(input())

def dfs(x):
    visited[x] = True
    if not visited[students[x]]: dfs(students[x])
    stack.append(x)

def re_dfs(x):
    visited[x] = True
    for next in re_adj[x]:
        if not visited[next]: re_dfs(next)
    each_group.append(x)

for _ in range(T):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    re_adj = [[] for _ in range(n + 1)]
    for each in range(1, n + 1):
        re_adj[students[each]].append(each)
    visited = [False for _ in range(n + 1)]

    stack = []
    for node in range(1, n + 1):
        if not visited[node]: dfs(node)

    visited = [False for _ in range(n + 1)]
    groups, each_group = [], []

    while stack:
        cur_node = stack.pop()
        if not visited[cur_node]:
            re_dfs(cur_node)
            groups.append(each_group)
            each_group = []

    answer = 0
    for each in groups:
        if len(each) > 1: answer += len(each)
        elif students[each[0]] == each[0]: answer += 1
    print(n - answer)