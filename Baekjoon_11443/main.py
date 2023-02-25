def mat_mul(A, B):
    tmp = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                tmp[i][j] += (A[i][k] * B[k][j]) % mod
    return tmp

def mat_pow(A, k):
    if k <= 1: return A
    tmp = mat_pow(A, k // 2)
    if k % 2: return mat_mul(mat_mul(tmp, tmp), A)
    else: return mat_mul(tmp, tmp)

n = int(input())
mod = 10 ** 9 + 7
mat = [[1, 1], [1, 0]]

if not n % 2: n += 1
res = mat_pow(mat, n + 1)
print((res[0][0] - res[0][1] - 1 + mod) % mod)