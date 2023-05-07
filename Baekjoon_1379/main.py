import sys
input = sys.stdin.readline

n = int(input())
closed_time = [0 for _ in range(n + 1)]
lecture_room = [-1 for _ in range(n + 1)]

arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[2]))
count = 0
for num, start, end in arr:
    for i in range(1, n + 1):
        if closed_time[i] <= start:
            closed_time[i] = end
            lecture_room[num] = i
            count = max(count, i)
            break
print(count)
for each in lecture_room[1:]: print(each)