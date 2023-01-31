T = int(input())
matrix = [[6, -4], [1, 0]]
MOD = 10 ** 3
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

for t in range(1, T + 1):
    x = int(input())
    print('Case #{}:'.format(t), end=' ')
    tmp = MatPower(matrix, x - 1)
    res = ((28 * tmp[1][0] + 6 * tmp[1][1] - 1) + MOD) % MOD
    print(str(res).zfill(3))
