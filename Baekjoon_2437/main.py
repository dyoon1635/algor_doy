n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 1
for each in arr:
    if result < each: break
    result += each
print(result)