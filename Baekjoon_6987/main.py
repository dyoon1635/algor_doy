from itertools import combinations

all_case, table = [], []
possible = 0
for x, y in combinations([0, 1, 2, 3, 4, 5], 2):
    all_case.append([x, y])

def make_table(league):
    res = []
    for i in range(0, 18, 3):
        res.append(league[i : i + 3])
    return res

def backtracking(idx):
    global possible, table
    if idx == 15:
        for team in table:
            for each_result in team:
                if each_result: return
        possible = 1
        return

    A, B = all_case[idx]
    # Win
    if table[A][0] and table[B][2]:
        table[A][0], table[B][2] = table[A][0] - 1, table[B][2] - 1
        backtracking(idx + 1)
        table[A][0], table[B][2] = table[A][0] + 1, table[B][2] + 1
    # Draw
    if table[A][1] and table[B][1]:
        table[A][1], table[B][1] = table[A][1] - 1, table[B][1] - 1
        backtracking(idx + 1)
        table[A][1], table[B][1] = table[A][1] + 1, table[B][1] + 1
    # Lose
    if table[A][2] and table[B][0]:
        table[A][2], table[B][0] = table[A][2] - 1, table[B][0] - 1
        backtracking(idx + 1)
        table[A][2], table[B][0] = table[A][2] + 1, table[B][0] + 1

for _ in range(4):
    league = list(map(int, input().split()))
    table = make_table(league)
    possible = 0
    backtracking(0)
    print(possible, end=' ')
