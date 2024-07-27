import sys, bisect
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

LIS = [arr[0]]
for each in arr[1:]:
    if each > LIS[-1]:
        LIS.append(each)
    else:
        idx = bisect.bisect_left(LIS, each)
        LIS[idx] = each

print(len(LIS))


