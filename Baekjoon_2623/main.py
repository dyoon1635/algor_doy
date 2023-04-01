import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]

for _ in range(m):
    tmp = list(map(int, input().split()))
    for idx in range(1, tmp[0]):
        each, next = tmp[idx], tmp[idx + 1]
        adj[each].append(next)
        indegree[next] += 1
topology = []
dq = deque()
for idx in range(1, n + 1):
    if indegree[idx] == 0:
        dq.append(idx)

while dq:
    cur = dq.popleft()
    topology.append(cur)
    for next in adj[cur]:
        indegree[next] -= 1
        if indegree[next] == 0:
            dq.append(next)

if len(topology) != n: print(0)
else:
    for each in topology: print(each)