n, m = map(int, input().split())
matrix = [[1, 1,], [1, 0]]
MOD = 10 ** 9 + 7
if n > m: n, m = m, n

def MatMul(mat1, mat2):
    tmp = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                tmp[i][j] += mat1[i][k] * mat2[k][j] % MOD
    return tmp

def PowerMat(mat, k):
    if k == 1: return mat
    tmp = PowerMat(mat, k // 2)
    if k % 2 ==0: return MatMul(tmp, tmp)
    return MatMul(MatMul(tmp, tmp), mat)

def GCD(a, b):
    if b == 0: return a
    return GCD(b, a % b)
print(PowerMat(matrix, GCD(m, n))[0][1] % MOD)