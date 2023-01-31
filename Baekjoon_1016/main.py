from math import *
m, M = map(int, input().split())
nums = [1 for i in range(m, M + 1)]

for each in range(2, int(sqrt(M)) + 1):
    tmp = each ** 2
    idx = m // tmp
    while tmp * idx <= M:
        n = tmp * idx
        if m <= n <= M: nums[n - m] = 0
        idx += 1
print(sum(nums))

