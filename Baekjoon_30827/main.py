import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
pq = []
room = [0 for _ in range(k)]
for _ in range(n):
    s, e = map(int, input().split())
    heapq.heappush(pq, (e, s))

count = 0
while pq:
    end, start = heapq.heappop(pq)
    time_diff, room_num = sys.maxsize, 0
    for idx, each_room_time in enumerate(room):
        if each_room_time < start:
            if start - each_room_time < time_diff:
                time_diff = start - each_room_time
                room_num = idx
    if time_diff < sys.maxsize:
        room[room_num] = end
        count += 1
print(count)