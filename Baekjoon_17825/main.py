board = [[1], [2], [3], [4], [5], [6, 21],
         [7], [8], [9], [10], [11, 25],
         [12], [13], [14], [15], [16, 27],
         [17], [18], [19], [20], [32],
         [22], [23], [24], [30],
         [26], [24], [28], [29], [24], [31], [20], [32]]
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
         22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
         13, 16, 19, 25, 22, 24,
         28, 27, 26, 30, 35, 0]

dice = list(map(int, input().split()))
answer = 0
def backtracking(result, h_loc, d_num):
    global answer
    if d_num == 10:
        answer = max(answer, result)
        return

    for i in range(4):
        d = dice[d_num]
        cur_pos, next_pos = h_loc[i], h_loc[i]
        if h_loc[i] == 32: continue
        if len(board[next_pos]) == 2:
            next_pos = board[next_pos][-1]
            d -= 1
        for _ in range(d):
            if next_pos == 32: break
            next_pos = board[next_pos][0]
        #print(cur_pos, '+', d, '-->', next_pos)
        if next_pos != 32 and next_pos in h_loc: continue

        h_loc[i] = next_pos
        backtracking(result + score[next_pos], h_loc, d_num + 1)
        h_loc[i] = cur_pos

backtracking(0,[0, 0, 0, 0], 0)
print(answer)