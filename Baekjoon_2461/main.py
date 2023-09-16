import heapq
from collections import deque

n, m = map(int, input().split())
school = [deque(sorted(list(map(int, input().split())))) for _ in range(n)]
pq = []

max_val, min_val = 0, 10 ** 9
for i in range(n):
    tmp = school[i].popleft()
    max_val, min_val = max(max_val, tmp), min(min_val, tmp)
    heapq.heappush(pq, (tmp, i))
result = max_val - min_val
while True:
    student, idx = heapq.heappop(pq)
    if not school[idx]: break

    new_student = school[idx].popleft()
    heapq.heappush(pq, (new_student, idx))
    max_val, min_val = max(max_val, new_student), pq[0][0]
    result = min(result, max_val - min_val)
print(result)