import sys
input = sys.stdin.readline

A, B, C, D = [], [], [], []
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

result = 0
AB = dict()
for a in A:
    for b in B:
        tmp = a + b
        if tmp in AB:
            AB[tmp] += 1
        else:
            AB[tmp] = 1
for c in C:
    for d in D:
        tmp = c + d
        if -tmp in AB:
            result += AB[-tmp]
print(result)