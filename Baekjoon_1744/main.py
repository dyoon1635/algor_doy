import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
if n == 1:
    print(arr[0])
    exit(0)
arr.sort()
result = [[0 for _ in range(n)] for _ in range(2)] # 0 : 안묶은 거, 1 : 묶은 거

result[0][0], result[1][0] = arr[0], arr[0]
result[0][1] = arr[0] + arr[1]
result[1][1] = arr[0] * arr[1]

for i in range(2, n):
    result[0][i] = max(result[0][i - 1] + arr[i],
                       result[1][i - 1] + arr[i])
    result[1][i] = max(result[0][i - 2] + arr[i - 1] * arr[i],
                       result[1][i - 2] + arr[i - 1] * arr[i])
print(max(result[0][-1], result[1][-1]))