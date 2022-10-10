import sys

MAX = 200001
def init():
    global dict, idx, parent
    dict, idx = {}, 0
    parent = [[i, 1] for i in range(200001)]

def union(a, b):
    a_idx, a_num = find(a)
    b_idx, b_num = find(b)
    if a_idx == b_idx:
        return parent[a_idx][1]
    parent[b_idx] = [a_idx, a_num + b_num]
    parent[a_idx][1] = a_num + b_num
    return parent[a_idx][1]

def find(x):
    if parent[x][0] == x: return parent[x]
    parent[x] = find(parent[x][0])
    return parent[x]

T = int(sys.stdin.readline())
for _ in range(T):
    init()
    F = int(sys.stdin.readline())
    for _ in range(F):
        A, B = sys.stdin.readline().split()
        if A not in dict:
            dict[A] = idx
            idx += 1
        if B not in dict:
            dict[B] = idx
            idx += 1
        print(union(dict[A], dict[B]))