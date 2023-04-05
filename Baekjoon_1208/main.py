import sys
from itertools import combinations
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr1, arr2 = arr[:n // 2], arr[n // 2:]

arr1_sum = []
arr2_sum = []
for cnt in range(len(arr1) + 1):
    for each_case in combinations(arr1, cnt):
        arr1_sum.append(sum(each_case))
for cnt in range(len(arr2) + 1):
    for each_case in combinations(arr2, cnt):
        arr2_sum.append(sum(each_case))
arr1_sum.sort()
arr2_sum.sort(reverse=True)

answer = 0
p1, p2 = 0, 0
while p1 < len(arr1_sum) and p2 < len(arr2_sum):
    s1, s2 = arr1_sum[p1], arr2_sum[p2]
    total = s1 + s2
    if total == s:
        p1_tmp, p2_tmp = p1, p2
        while p1_tmp < len(arr1_sum) and arr1_sum[p1_tmp] == s1:
            p1_tmp += 1
        while p2_tmp < len(arr2_sum) and arr2_sum[p2_tmp] == s2:
            p2_tmp += 1
        answer += (p1_tmp - p1) * (p2_tmp - p2)
        p1, p2 = p1_tmp, p2_tmp
    elif total > s: p2 += 1
    else: p1 += 1
print(answer - 1 if s == 0 else answer)