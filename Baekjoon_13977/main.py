import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7

n = 4 * (10 ** 6)
factorial = [1 for _ in range(n + 1)]
for i in range(1, n + 1):
    factorial[i] = (factorial[i - 1] * i) % MOD

m = int(input())
for _ in range(m):
    n, k = map(int, input().split())
    A = factorial[n]
    B = (factorial[k] * factorial[n - k]) % MOD

    B1 = 1
    expo = MOD - 2
    while expo:
        if expo % 2:
            B1 = (B * B1) % MOD
        B = (B * B) % MOD
        expo //= 2
    print((A * B1) % MOD)