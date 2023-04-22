import sys
input = sys.stdin.readline
MOD = 10 ** 6 + 3

def mat_power(mat, k):
    if k == 1: return mat
    tmp = mat_power(mat, k // 2)
    if k % 2 == 0:
        return mat_mul(tmp, tmp)
    return mat_mul(mat_mul(tmp, tmp), mat)

def mat_mul(mat1, mat2):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += (mat1[i][k] * mat2[k][j]) % MOD
    return tmp

n, s, e, t = map(int, input().split())
N = 5 * n
m = [[0] * (N) for _ in range(N)]
for i in range(n):
    for j in range(1, 5):
        m[5 * i + j - 1][5 * i + j] = 1

for i in range(n):
    tmp = list(map(int, input().strip()))
    for j in range(n):
        if tmp[j] > 0:
            m[5 * i + tmp[j] - 1][5 * j] = 1

print(mat_power(m, t)[5 * (s - 1)][5 * (e - 1)] % MOD)

