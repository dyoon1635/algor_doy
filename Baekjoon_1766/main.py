import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    indegree[b] += 1

topology = []
q = []
for i in range(1, n + 1):
    if not indegree[i]: q.append(i)
heapq.heapify(q)
while q:
    cur = heapq.heappop(q)
    topology.append(cur)
    for next in adj[cur]:
        indegree[next] -= 1
        if not indegree[next]:
            heapq.heappush(q, next)

print(*topology)
