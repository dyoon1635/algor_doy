def make_table(pattern):
    length = len(pattern)

    arr = [0 for _ in range(length)]
    pidx = 0
    for idx in range(1, length):
        while pidx > 0 and pattern[idx] != pattern[pidx]:
            pidx = arr[pidx - 1]
        if pattern[idx] == pattern[pidx]:
            pidx += 1
            arr[idx] = pidx
    return arr

n = int(input())
pattern_table = make_table(input())
print(n - pattern_table[-1])