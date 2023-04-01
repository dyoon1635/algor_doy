n = int(input())
potions = list(map(int, input().split()))

lp, rp = 0, n - 1
x, y = potions[lp], potions[rp]
total = x + y

while lp < rp:
    tmp = potions[lp] + potions[rp]
    if abs(tmp) <= abs(total):
        x, y = potions[lp], potions[rp]
        total = tmp

    if tmp == 0: break
    elif tmp < 0: lp += 1
    elif tmp > 0: rp -= 1
print(x, y)
