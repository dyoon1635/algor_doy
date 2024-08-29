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

while True:
    word = input()
    if word == '.':
        break

    pattern_table = make_table(word)
    length = len(word)
    div, mod = divmod(length, length - pattern_table[-1])
    print(1 if mod else div)
