import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(cur_node, pre_node):
    global answer
    max_depth = 0
    for next_node in adj[cur_node]:
        if next_node != pre_node:
            max_depth = max(max_depth, dfs(next_node, cur_node))
    if max_depth >= d: answer += 1
    return max_depth + 1

n, s, d = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
answer = 0
dfs(s, 0)
print(max(2 * (answer - 1), 0))