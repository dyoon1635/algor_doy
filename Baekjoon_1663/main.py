n, x = int(input()), int(input())
length = [0] * 101
cnt = [[0] * 3 for _ in range(101)] # step일 떄 XYZ의 각각 개수
base = [None, 'X', 'YZ', 'ZX']

length[1], length[2], length[3] = 1, 2, 2
cnt[1][0] = 1
cnt[2][1], cnt[2][2] = 1, 1
cnt[3][0], cnt[3][2] = 1, 1

for i in range(4, x + 1):
    length[i] = length[i - 3] + length[i - 2]
    for j in range(3):
        cnt[i][j] = cnt[i - 3][j] + cnt[i - 2][j]

def solve(idx, step):
    if step <= 3: return base[step][idx - 1]
    if length[step - 3] >= idx: return solve(idx, step - 3)
    else: return solve(idx - length[step - 3], step - 2)

if n == 1:
    print(length[x])
elif n == 2:
    k = int(input())
    print(solve(k, x))
elif n == 3:
    c = input()
    print(cnt[x][ord(c) - ord('X')])

