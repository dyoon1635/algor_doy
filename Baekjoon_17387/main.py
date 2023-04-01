def ccw(p1, p2, p3):
    tmp = (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - \
          (p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1])
    if tmp == 0: return 0
    return 1 if tmp > 0 else -1

def check(p1, p2, p3):
    if p1[0] < p2[0]: return p2[0] < p3[0]
    elif p2[0] < p1[0]: return p3[0] < p2[0]
    else:
        if p1[1] < p2[1]: return p2[1] < p3[1]
        elif p2[1] < p1[1]: return p3[1] < p2[1]

def intersect():
    p1, p2 = (x1, y1), (x2, y2)
    p3, p4 = (x3, y3), (x4, y4)

    std1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    std2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)
    if std1 == 0 and std2 == 0:
        return not ((check(p1, p2, p3) and check(p1, p2, p4)) \
                    or (check(p2, p1, p3) and check(p2, p1, p4)))
    else: return std1 <= 0 and std2 <= 0


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

print(1 if intersect() else 0)