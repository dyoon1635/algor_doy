import sys
from collections import deque

def dijkstra():
    q = deque()
    q.append([s, 0])
    while q:
        cur_node, cur_cost = q.popleft()
        if cur_node == d: continue
        for each in adj[cur_node]:
            next_node, next_cost = each, adj[cur_node][each]
            new_cost = cur_cost + next_cost
            if new_cost > distance[next_node]: continue
            if new_cost == distance[next_node]:
                edge[next_node].append(cur_node)
            else:
                edge[next_node] = [cur_node]
                distance[next_node] = new_cost
                q.append([next_node, new_cost])

def delete():
    q = deque()
    for each in edge[d]:
        q.append([d, each])
    while q:
        cur_node, ex_node = q.popleft()
        if cur_node == s: break
        adj[ex_node][cur_node] = sys.maxsize
        while edge[ex_node]:
            q.append([ex_node, edge[ex_node].pop()])

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0: break
    s, d = map(int, sys.stdin.readline().split())
    adj = [dict() for _ in range(n)]
    distance = [sys.maxsize for i in range(n)]; distance[s] = 0
    edge = [[] for _ in range(n)]

    for _ in range(m):
        u, v, p = map(int, sys.stdin.readline().split())
        adj[u][v] = p
    dijkstra()
    delete()
    distance = [sys.maxsize for i in range(n)]
    dijkstra()
    print(distance[d] if distance[d] != sys.maxsize else -1)