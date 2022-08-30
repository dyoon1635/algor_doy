import sys

cnt = 0
n = int(sys.stdin.readline())
arr = list(list(map(int, sys.stdin.readline().split())))

def MergeSort(start, end):
    global cnt, arr
    if start < end:
        mid = (start + end) // 2
        MergeSort(start, mid)
        MergeSort(mid + 1, end)

        a, b = start, mid + 1
        tmp = []
        while a <= mid and b <= end:
            if arr[a] <= arr[b]:
                tmp.append(arr[a])
                a += 1
            else:
                tmp.append(arr[b])
                b += 1
                cnt += (mid - a + 1)
        if a <= mid: tmp += arr[a:mid + 1]
        if b <= end: tmp += arr[b:end + 1]

        for i in range(len(tmp)):
            arr[start + i] = tmp[i]

MergeSort(0, n - 1)
print(cnt)