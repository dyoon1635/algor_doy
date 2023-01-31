n = int(input())
matrix = [[1, 1], [1, 0]]
MOD = 10 ** 6
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
res = MatPower(matrix, n)
print(res[0][1] % MOD)