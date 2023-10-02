n = int(input())
arr = list(sorted(list(map(int, input().split()))))
lp, rp = 0, n - 1
res = arr[lp] + arr[rp]

while lp < rp:
    new = arr[lp] + arr[rp]
    if abs(res) > abs(new): res = new
    if new < 0: lp += 1
    else: rp -= 1
print(res)