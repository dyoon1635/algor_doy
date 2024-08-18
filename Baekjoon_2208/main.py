import sys
input = sys.stdin.readline

n, m = map(int, input().split())
jewel = [int(input()) for _ in range(n)]
sum_arr = [jewel[i] for i in range(n)]
for i in range(1, n):
    sum_arr[i] += sum_arr[i - 1]

result, tmp = 0, 0
for i in range(m - 1, n - 1):
    tmp = min(tmp, sum_arr[i - m + 1])
    result = max(result, sum_arr[i + 1] - tmp)
print(result)