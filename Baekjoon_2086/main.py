n, m = map(int, input().split())
matrix = [[1, 1], [1, 0]]
MOD = 10 ** 9
def MatMul(mat1, mat2):
    tmp = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                tmp[i][j] += mat1[i][k] * mat2[k][j] % MOD
    return tmp

def MatPower(mat, k):
    if k == 1: return mat
    tmp = MatPower(mat, k // 2)
    if k % 2 == 0: return MatMul(tmp, tmp)
    return MatMul(MatMul(tmp, tmp), mat)
a = MatPower(matrix, n + 1)[0][1] % MOD
b = MatPower(matrix, m + 2)[0][1] % MOD
print(((b - a) + MOD) % MOD)