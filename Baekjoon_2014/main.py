import heapq

k, n = map(int, input().split())
prime = list(map(int, input().split()))
pq = []
for each in prime:
    heapq.heappush(pq, each)
tmp = None
for i in range(n):
    tmp = heapq.heappop(pq)
    for each in prime:
        heapq.heappush(pq, tmp * each)
        if not tmp % each: break
print(tmp)