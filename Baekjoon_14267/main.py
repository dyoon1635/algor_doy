import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(node, s):
    emp_score[node] += (s + score[node])
    for next_node in adj[node]:
        dfs(next_node, s + score[node])

n, m = map(int, input().split())
emp = list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]
for idx in range(1, n):
    adj[emp[idx]].append(idx + 1)

score = [0 for _ in range(n + 1)]
for _ in range(m):
    x, w = map(int, input().split())
    score[x] += w

emp_score = [0 for _ in range(n + 1)]
dfs(1, 0)
print(*emp_score[1:])