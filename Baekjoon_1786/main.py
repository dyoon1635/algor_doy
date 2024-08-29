def make_table(string):
    length = len(string)
    arr = [0 for _ in range(length)]
    pidx = 0
    for idx in range(1, length):
        while pidx > 0 and string[pidx] != string[idx]:
            pidx = arr[pidx - 1]
        if string[idx] == string[pidx]:
            pidx += 1
            arr[idx] = pidx
    return arr

def KMP(word, pattern):
    pidx = 0
    result = []
    for idx in range(len(word)):
        while pidx > 0 and word[idx] != pattern[pidx]:
            pidx = pattern_table[pidx - 1]
        if word[idx] == pattern[pidx]:
            if pidx == len(pattern) - 1:
                result.append(idx - len(pattern) + 2)
                pidx = pattern_table[pidx]
            else:
                pidx += 1
    print(len(result))
    for each_idx in result:
        print(each_idx)

T, P = input(), input()
pattern_table = make_table(P)
KMP(T, P)