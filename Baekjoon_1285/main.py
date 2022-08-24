import copy
n = int(input())
coin = []
for _ in range(n):
    coin.append(list(input()))
answer = n ** 2

for bit in range(1 << n):
    #tmp = copy.deepcopy(coin)
    tmp = [coin[i] for i in range(n)]
    for i in range(n):
        if bit & (1 << i):
            for j in range(n):
                if tmp[i][j] == 'H': tmp[i][j] = 'T'
                else: tmp[i][j] = 'H'

    res = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if tmp[j][i] == 'T': cnt += 1
        res += min(cnt, n - cnt)
    answer = min(answer, res)
print(answer)