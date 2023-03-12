import sys
input = sys.stdin.readline

n = int(input())
potions = sorted(list(map(int, input().split())))

result = [(0, 1, 2), sys.maxsize]
for i in range(n - 2):
    lp, rp = i + 1, n - 1
    while lp < rp:
        total = potions[i] + potions[lp] + potions[rp]

        if abs(total) < result[1]:
            result = [(i, lp, rp), abs(total)]

        if total < 0: lp += 1
        elif total > 0: rp -= 1
        else: break
    if result[1] == 0: break
for each in result[0]:
    print(potions[each], end=' ')