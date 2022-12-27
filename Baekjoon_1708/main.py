import sys
input = sys.stdin.readline

def inclination(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])

def ccw(p1, p2, p3):
    v, u = inclination(p1, p2), inclination(p2, p3)
    if v[0] * u[1] > v[1] * u[0]: return True
    return False

def convex_hull():
    global answer
    convex = []
    for p3 in pos:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1, p2, p3): break
            convex.pop()
        convex.append(p3)
    answer += (len(convex) - 1)

n = int(input())
pos = []
answer = 0
for _ in range(n):
    pos.append(list(map(int, input().split())))
pos.sort()
convex_hull()
pos.reverse()
convex_hull()
print(answer)