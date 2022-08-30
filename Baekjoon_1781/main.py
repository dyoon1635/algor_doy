import heapq, sys
n = int(sys.stdin.readline())
total, possible = [], []
day = 0
for _ in range(n):
    deadline, ramen = map(int, sys.stdin.readline().split())
    heapq.heappush(total, (-deadline, -ramen)) # deadline desc, cost desc
    day = max(day, deadline)

res = 0
while total or possible:
    if total and -total[0][0] >= day:
        d, r = heapq.heappop(total)
        heapq.heappush(possible, (r, d))
        continue
    if not possible:
        day -= 1
    while possible:
        r, d = heapq.heappop(possible)
        if 1 <= day <= -d:
            res += r
            day -= 1
            break
print(-res)