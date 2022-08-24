import sys, heapq

n = int(sys.stdin.readline())
# i번쨰 건문의 높이, 끝점
height, end, arr = [0] * n, [0] * n, []
check = set() # 현재까지 끝난 끝점 저장

for i in range(n):
    l, h, r = map(int, sys.stdin.readline().split())
    arr.append((l, i, 1)) # 시작점
    arr.append((r, i, -1)) # 끝점
    height[i], end[i] = h, r

# 1st priority : 시점이 앞서는지
# 2nd priority : 시작점인지
# 3nd priority : 높이가 더 높은지
arr.sort(key=lambda x: (x[0], -x[2], -height[x[1]]))

now = 0 # 현재 최고 높이
ans, q = [], []
for i in range(len(arr)):
    point, idx, dir = arr[i]
    if dir == 1: # 시작점인경우
        if now < height[idx]: # 높이 갱신
            now = height[idx]
            ans.append((point, now))
        # 현재 건물의 높이와 끝점 저장
        heapq.heappush(q, (-height[idx], end[idx]))
    else: # 끝점인 경우
        check.add(point)
        while q:
            # 최대 높이가 끝난 건물이 아닐 때까지 pop
            if q[0][1] not in check: break
            heapq.heappop(q)
        if not q:
            # 힙이 비었으면 현재 높이 0으로 초기화
            if now:
                now = 0
                ans.append((point, now))
        else:
            if -q[0][0] != now:
                now = -q[0][0]
                ans.append((point, now))
for each in ans: print(each[0], each[1], end=' ')
