import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

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
    scc_num[node] = num

def answer():
    for i in range(1, n + 1):
        if scc_num[i] == scc_num[-i]:
            print(0)
            exit(0)
    return 1

n, m = map(int, input().split())
N = 2 * n
adj = [[] for _ in range(N + 1)]
re_adj = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[-a].append(b)
    adj[-b].append(a)

    re_adj[b].append(-a)
    re_adj[a].append(-b)

stack = deque()
for node in range(1, N + 1):
    if not visited[node]:
        dfs(node)

visited = [False for _ in range(N + 1)]
SCC, each_SCC = [], []
num = 0
scc_num = [-1 for _ in range(N + 1)]
while stack:
    cur_node = stack.pop()
    if not visited[cur_node]:
        num += 1
        re_dfs(cur_node)

result = [1 for _ in range(N + 1)]
for i in range(1, n + 1):
    if scc_num[i] < scc_num[-i]:
        result[i] = 0
#print(scc_num)
print(answer())
print(*result[1:n + 1])