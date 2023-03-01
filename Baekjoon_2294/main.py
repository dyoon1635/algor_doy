import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
dp = [sys.maxsize for _ in range(100000 + 1)]
for _ in range(n):
    coin = int(input())
    dp[coin] = 1
    coins.append(coin)

for i in range(1, k + 1):
    for each_coin in coins:
        if i - each_coin > 0:
            dp[i] = min(dp[i], dp[i - each_coin] + 1)
print(dp[k] if dp[k] < sys.maxsize else -1)