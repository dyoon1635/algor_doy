n = int(input())
matrix = [[1, 1], [1, 0]]
MOD = 10 ** 9 + 7
def mat_mul(mat1, mat2):
    tmp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                tmp[i][j] += mat1[i][k] * mat2[k][j] % MOD
    return tmp

def mat_power(mat, N):
    if N == 1: return mat
    tmp = mat_power(mat, N // 2)
    if not N % 2: return mat_mul(tmp, tmp)
    return mat_mul(mat_mul(tmp, tmp), mat)

result = mat_power(matrix, n)
#print(result[0][1] % MOD) 11444
print((result[0][0] * result[0][1]) % MOD)