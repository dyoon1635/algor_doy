n = int(input())
honey = list(map(int, input().split()))
subsum = [honey[0]] + [0 for _ in range(n - 1)]

for i in range(1, n):
    subsum[i] = subsum[i - 1] + honey[i]

result = 0

for bee in range(1, n - 1): # left
    result = max(result,
                 subsum[bee - 1] * 2 + subsum[-2] - subsum[bee])
for bee in range(1, n - 1): # right
    result = max(result,
                 subsum[-1] - honey[0] - honey[bee] +
                 subsum[-1] - subsum[bee])
for honey_pot in range(1, n - 1): # mid
    result = max(result,
                 subsum[-2] - honey[0] + honey[honey_pot])
print(result)