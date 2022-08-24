n = int(input())
nums = list(map(int, input().split()))
num_cnt = [0] * 1003
for num in nums:
    num_cnt[num] += 1

cur, result = 0, []
while n > 0:
    if num_cnt[cur]:
        if num_cnt[cur + 1]:
            for i in range(cur + 2, 1001):
                if num_cnt[i]:
                    result.extend([cur] * num_cnt[cur])
                    result.extend([i])
                    n -= (num_cnt[cur] + 1)
                    num_cnt[i] -= 1
                    break
            else:
                result.extend([cur + 1] * num_cnt[cur + 1])
                result.extend([cur] * num_cnt[cur])
                n -= (num_cnt[cur] + num_cnt[cur + 1])
                num_cnt[cur + 1] = 0
        else:
            result.extend([cur] * num_cnt[cur])
            n -= num_cnt[cur]
        num_cnt[cur] = 0
    cur += 1
print(*result)