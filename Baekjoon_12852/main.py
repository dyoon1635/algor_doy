import sys
n = int(input())
dp = [sys.maxsize for _ in range(n + 1)]
dp[0], dp[1] = 0, 0

for i in range(2, n + 1):
    if i % 2 == 0:
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i - 1], dp[i // 2], dp[i // 3]) + 1
        else:
            dp[i] = min(dp[i], dp[i - 1], dp[i // 2]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i], dp[i - 1], dp[i // 3]) + 1
    else:
        dp[i] = min(dp[i], dp[i - 1]) + 1

result = [n]
cur_num = n
while True:
    if cur_num == 1: break

    if dp[cur_num] == dp[cur_num - 1] + 1:
        result.append(cur_num - 1)
        cur_num -= 1
    elif cur_num % 2 == 0 and dp[cur_num] == dp[cur_num // 2] + 1:
        result.append(cur_num // 2)
        cur_num //= 2
    elif cur_num % 3 == 0 and dp[cur_num] == dp[cur_num // 3] + 1:
        result.append(cur_num // 3)
        cur_num //= 3

print(dp[n])
print(*result)