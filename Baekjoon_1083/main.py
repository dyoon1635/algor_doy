n = int(input())
arr = list(map(int, input().split()))
s = int(input())

i = 0
while s > 0 and i < n:
    idx = arr.index(max(arr[i : i + s + 1]))
    num = arr[idx]
    if idx != i:
       del arr[idx]
       arr.insert(i, num)
       s -= (idx - i)
    else:
        i += 1
print(*arr)