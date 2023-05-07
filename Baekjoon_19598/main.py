import sys, heapq
input = sys.stdin.readline

room = [0 for _ in range(100001)]
lecture = []

n = int(input())
for _ in range(n):
    s, e = map(int, input().split())
    heapq.heappush(lecture, (s, e))

while lecture:
    s, e = heapq.heappop(lecture)
    for idx, each_room in enumerate(room):
        if each_room <= s:
            room[idx] = e
            break
count = 0
for each_room in room:
    if each_room == 0: break
    count += 1
print(count)
