import sys, heapq
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    h, o = map(int, input().split())
    if h > o: h, o = o, h
    arr.append((h, o))
arr.sort(key=lambda x: x[1])
road = int(input())
cur, answer = 0, 0
pq = []
for home, office in arr:
    if abs(home - office) > road: continue
    cur = office
    heapq.heappush(pq, (home, office))
    while pq and cur - pq[0][0] > road:
        heapq.heappop(pq)
    answer = max(answer, len(pq))
print(answer)