import sys
input = sys.stdin.readline

def backtracking(idx):
    global answer
    if idx == n:
        count = 0
        for s, w in eggs:
            if s <= 0: count += 1
        answer = max(answer, count)
        return

    if eggs[idx][0] <= 0: backtracking(idx + 1)
    else:
        check = True
        for i, (s, w) in enumerate(eggs):
            if i == idx or s <= 0: continue
            check = False
            eggs[idx][0] -= w
            eggs[i][0] -= eggs[idx][1]
            backtracking(idx + 1)
            eggs[idx][0] += w
            eggs[i][0] += eggs[idx][1]
        if check: backtracking(n)

n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]

answer = 0
backtracking(0)
print(answer)