n = int(input())
nums = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

idx = max(dp)
result = []
for i in reversed(range(n)):
    if idx == 0: break

    if idx == dp[i]:
        result.append(nums[i])
        idx -= 1

print(len(result))
print(*reversed(result))