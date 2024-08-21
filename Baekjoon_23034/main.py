import sys, heapq
from collections import deque
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[max(x, y)] = min(x, y)

def kruskal():
    count, result = 0, 0
    while pq:
        cost, a, b = heapq.heappop(pq)
        pa, pb = find(a), find(b)
        if pa == pb:
            continue
        union(pa, pb)
        adj[a].append((b, cost))
        adj[b].append((a, cost))
        count += 1
        result += cost
        if count == n - 1:
            break
    return result

def bfs(start):
    dist[start][start] = 0
    dq = deque([(start, 0)])
    while dq:
        node, max_cost = dq.popleft()
        for next, cost in adj[node]:
            if dist[start][next] > 0:
                continue
            next_cost = max(max_cost, cost)
            dist[start][next] = next_cost
            dq.append((next, next_cost))

if __name__ == "__main__":
    n, m = map(int, input().split())
    pq = []
    adj = [[] for _ in range(n + 1)]
    dist = [[-1] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        heapq.heappush(pq, (c, a, b))

    parent = [i for i in range(n + 1)]
    total = kruskal()

    for each in range(1, n + 1):
        bfs(each)

    for _ in range(int(input())):
        x, y = map(int, input().split())
        print(total - dist[x][y])

