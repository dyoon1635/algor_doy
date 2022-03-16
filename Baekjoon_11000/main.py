import heapq

n = int(input())
course = []
classroom = []
for _ in range(n):
    start, end = map(int, input().split())
    course.append([start, end])
course.sort()

classroom.append(course[0][1])
for i in range(1, n):
    if classroom[0] <= course[i][0]:
        heapq.heappop(classroom)
    heapq.heappush(classroom, course[i][1])
print(len(classroom))