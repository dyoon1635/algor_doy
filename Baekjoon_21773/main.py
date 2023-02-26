import heapq, sys
input = sys.stdin.readline
print = sys.stdout.write

T, N = map(int, input().split())
pq = []
for _ in range(N):
    pid, t, p = map(int, input().split()) # pid, time, priority
    heapq.heappush(pq, (-p, pid, t)) # priority desc, pid, time

for _ in range(T):
    if not pq: break
    p, pid, t = heapq.heappop(pq)
    print(str(pid) + '\n')
    if t - 1 > 0: heapq.heappush(pq, (p + 1, pid, t - 1))
