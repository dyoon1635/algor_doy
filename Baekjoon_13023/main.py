import sys
n, m = map(int, input().split())
network = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    network[x].append(y)
    network[y].append(x)

def dfs(cur, mov):
    if mov >= 4:
        print(1)
        exit(0)
    for i in network[cur]:
        if not visited[i]:
            visited[i] = True
            dfs(i, mov + 1)
            visited[i] = False

if __name__ == "__main__":
    for i in range(n):
        visited[i] = True
        dfs(i, 0)
        visited[i] = False
    print(0)