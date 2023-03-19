import sys, heapq
input = sys.stdin.readline

c, n = map(int, input().split())
A = []
for _ in range(c):
    A.append([int(input()), False])
A.sort()

T = []
for _ in range(n):
    a, b = map(int, input().split())
    T.append((a, b))
T.sort(key=lambda x: (x[1], x[0]))

answer = 0
for Ts, Te in T:
    for idx, (chick, used) in enumerate(A):
        if Ts <= chick <= Te and not used:
            answer += 1
            A[idx][1] = True
            break
print(answer)

