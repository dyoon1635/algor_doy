N = int(input())
MOD = 10007
nCk = [[0] * 53 for _ in range(53)]

for n in range(53):
    nCk[n][0] = 1
    nCk[n][n] = 1
    for k in range(1, n):
        nCk[n][k] = (nCk[n - 1][k] + nCk[n - 1][k - 1]) % MOD
        nCk[n][n - k] = nCk[n][k]

answer = 0
for i in range(4, N + 1, 4):
    if (i // 4) % 2:
        answer += nCk[13][i // 4] * nCk[52 - i][N - i]
    else:
        answer -= nCk[13][i // 4] * nCk[52 - i][N - i]
    answer %= MOD
print((answer + MOD) % MOD)