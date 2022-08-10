import sys
from collections import deque
t = int(input())

def solve(n):
    if n == 1: return 1
    visited = [False] * n
    visited[1] = True
    dq = deque()
    dq.append(['1', 1]) # num ,mod
    while dq:
        num, mod = dq.popleft()
        for i in [0, 1]:
            m = (mod * 10 + i) % n
            if visited[m]: continue
            visited[m] = True
            if m == 0:
                return num + str(i)
            dq.append([num + str(i), m])

if __name__ == "__main__":
    for _ in range(t):
        x = int(sys.stdin.readline())
        print(solve(x))