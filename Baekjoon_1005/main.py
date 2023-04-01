import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))
    adj = [[] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]

    for _ in range(k):
        x, y = map(int, input().split())
        adj[x].append(y)
        indegree[y] += 1
    w = int(input())

    dq = deque()
    result = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if indegree[i] == 0:
            dq.append(i)
            result[i] = build_time[i]

    while dq:
        cur = dq.popleft()
        for next in adj[cur]:
            indegree[next] -= 1
            result[next] = max(result[next],
                               result[cur] + build_time[next])
            if indegree[next] == 0:
                dq.append(next)
    print(result[w])