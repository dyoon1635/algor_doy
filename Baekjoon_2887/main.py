import sys

n = int(input())
x_pos, y_pos, z_pos = [], [], []
for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    x_pos.append([x, i])
    y_pos.append([y, i])
    z_pos.append([z, i])
parent = [i for i in range(n)]
edge = []
answer = 0

def find(x):
    if x != parent[x]: parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    if a < b: parent[b] = a
    else: parent[a] = b

def MST(pos):
    global edge
    pos.sort()
    for i in range(n - 1):
        edge.append([pos[i][1], pos[i + 1][1], abs(pos[i][0] - pos[i + 1][0])])
    edge.sort(key=lambda x: x[2])

if __name__ == "__main__":
    MST(x_pos)
    MST(y_pos)
    MST(z_pos)
    for A, B, cost in edge:
        a, b = find(A), find(B)
        if a != b:
            union(A, B)
            answer += cost
    print(answer)