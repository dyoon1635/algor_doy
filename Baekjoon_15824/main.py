MOD = 10 ** 9 + 7
n = int(input())
arr = sorted(list(map(int, input().split())))

def pow(a, b):
    if b == 0: return 1
    if b == 1: return a

    tmp = pow(a, b // 2)
    if b % 2 == 0:
        return (tmp * tmp) % MOD
    else:
        return (tmp * tmp * a) % MOD

answer = 0
for i in range(n):
    answer += arr[i] * (pow(2, i) - pow(2, n - i - 1))
print(answer % MOD)