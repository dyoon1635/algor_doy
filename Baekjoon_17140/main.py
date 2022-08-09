import copy

r, c, k = map(int, input().split())

def make_row(dict):
    dict = sorted(dict.items(), key=lambda item: (item[1], item[0]))
    res = []
    for each in dict:
        res.append(each[0])
        res.append(each[1])
    return res

def rotate(A):
    new_A = [[0] * len(A) for _ in range(len(A[0]))]
    for y in range(len(A[0])):
        for x in range(len(A)):
            new_A[y][x] = A[x][y]
    return new_A

def R(A):
    new_A = []
    length = 0
    for row in A:
        tmp = {}
        for each in row:
            if each == 0: continue

            if each in tmp: tmp[each] += 1
            else: tmp[each] = 1
        new_row = make_row(tmp)
        new_A.append(new_row)
        length = max(length, len(new_row))

    for i in range(len(new_A)):
        while len(new_A[i]) < length:
            new_A[i] += [0]
    return new_A

def C(A):
    new_A = []
    length = 0
    for y in range(len(A[0])):
        tmp = {}
        for x in range(len(A)):
            if A[x][y] == 0: continue

            if A[x][y] in tmp: tmp[A[x][y]] += 1
            else: tmp[A[x][y]] = 1
        new_row = make_row(tmp)
        new_A.append(new_row)
        length = max(length, len(new_row))

    for i in range(len(new_A)):
        while len(new_A[i]) < length:
            new_A[i] += [0]

    return rotate(new_A)

def printf(A):
    for row in A: print(row)

if __name__ == "__main__":
    cnt = 0
    A = []
    for _ in range(3):
        A.append(list(map(int, input().split())))

    while cnt <= 100:
        row_num, col_num = len(A), len(A[0])
        if r - 1 < row_num and c - 1 < col_num \
                and A[r - 1][c - 1] == k:
            break

        if row_num >= col_num: A = R(A)
        else: A = C(A)
        cnt += 1

    if cnt <= 100: print(cnt)
    else: print(-1)