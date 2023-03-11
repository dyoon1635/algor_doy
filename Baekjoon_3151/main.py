from collections import Counter

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
num_count = Counter(nums)

result = 0
for idx, each in enumerate(nums):
    left, right = idx + 1, n - 1
    while left < right:
        tmp_sum = nums[left] + nums[right] + each
        if tmp_sum > 0: right -= 1
        elif tmp_sum < 0: left += 1
        else: # sum is zero
            if nums[left] == nums[right]:
                result += (right - left)
            else:
                result += (num_count[nums[right]])
            left += 1
print(result)