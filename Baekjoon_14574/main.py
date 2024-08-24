import sys, heapq, math
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[y] = x

def make_graph():
    arr = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            cost = math.floor((cook[i][1] + cook[j][1]) / abs(cook[i][0] - cook[j][0]))
            heapq.heappush(arr, (-cost, i, j))
    return arr

def kruskal():
    count, result = 0, 0
    while pq:
        cost, x, y = heapq.heappop(pq)

        px, py = find(x), find(y)
        if px != py:
            union(px, py)
            count += 1
            result -= cost
            adj[x].append(y)
            adj[y].append(x)

        if count == n - 1:
            break
    return result

def dfs(node):
    visited[node] = True
    for next in adj[node]:
        if not visited[next]:
            dfs(next)
            print(node, next)

if __name__ == "__main__":
    n = int(input())
    parent = [i for i in range(n + 1)]
    cook = [(-1, -1)]
    adj = [[] * (n + 1) for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    for i in range(n):
        p, c = map(int, input().split())
        cook.append((p, c))
    pq = make_graph()
    print(kruskal())
    dfs(1)
