import heapq
from collections import deque
MAX = 10 ** 5
n, k = map(int, input().split())
pq = [(0, n)] # time, location
visited = [False for _ in range(MAX + 1)]
while pq:
    t, x = heapq.heappop(pq)
    #print(t, x)
    if x == k:
        print(t)
        break

    if x * 2 <= MAX and not visited[x * 2]:
        heapq.heappush(pq, (t, x * 2)); visited[x * 2] = True
    if x + 1 <= MAX and not visited[x + 1]:
        heapq.heappush(pq, (t + 1, x + 1)); visited[x + 1] = True
    if x - 1 >= 0 and not visited[x - 1]:
        heapq.heappush(pq, (t + 1, x - 1)); visited[x - 1] = True