import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    indegree[b] += 1

dq = deque()
for idx in range(1, n + 1):
    if indegree[idx] == 0: dq.append(idx)

topology = []
while dq:
    cur_student = dq.popleft()
    topology.append(cur_student)

    for next in adj[cur_student]:
        indegree[next] -= 1
        if indegree[next] == 0:
            dq.append(next)
print(*topology)


