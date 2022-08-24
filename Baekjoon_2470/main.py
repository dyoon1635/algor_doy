n = int(input())
data = list(map(int, input().split()))
data.sort()
lp, rp = 0, n - 1
answer = [data[lp], data[rp]]
min_val = 1e+10

while lp < rp:
    _sum_ = data[lp] + data[rp]
    if min_val > abs(_sum_):
        min_val = abs(_sum_)
        answer = [data[lp], data[rp]]
        if sum == 0: break

    if _sum_ < 0: lp += 1
    else: rp -= 1
print(answer[0], answer[1])