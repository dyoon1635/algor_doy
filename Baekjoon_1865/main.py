import sys
input = sys.stdin.readline
inf = sys.maxsize

def solve(start):
    distance = [inf for _ in range(n + 1)]
    distance[start] = 0
    for i in range(n):
        for s, e, t in vertex:
            if distance[e] > distance[s] + t:
                distance[e] = distance[s] + t
                if i == n - 1: return True
    return False

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    vertex = []


    for _ in range(m):
        s, e, t = map(int, input().split())
        vertex.append((s, e, t))
        vertex.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        vertex.append((s, e, -t))
    print('YES' if solve(1) else 'NO')
