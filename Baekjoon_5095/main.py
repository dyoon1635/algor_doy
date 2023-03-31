import sys
#sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def mat_power(mat1, x):
    if x == 1: return mat1
    tmp = mat_power(mat1, x // 2)
    if x % 2 == 0: return mat_mul(tmp, tmp)
    else: return mat_mul(mat_mul(tmp, tmp), mat1)

def mat_mul(mat1, mat2):
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                tmp[i][j] += (mat1[i][k] * mat2[k][j]) % m
            tmp[i][j] = tmp[i][j] % m
    return tmp

def mat_print(mat1):
    for each in mat1: print(*each)

while True:
    n, m, p = map(int, input().split())
    if n == 0 and m == 0 and p == 0: break
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))
    mat_print(mat_power(mat, p))
    print('')