EMPTY = 100001
n = int(input())
dq = [EMPTY for _ in range(4)]
arr = list(map(int, input().split()))

for each in arr:
    possible = False
    for i in range(4):
        if dq[i] == EMPTY:
            dq[i] = each
            possible = True
            break
        elif dq[i] <= each:
            dq[i] = each
            possible = True
            break
    if not possible:
        print('NO')
        exit(0)
print('YES')
