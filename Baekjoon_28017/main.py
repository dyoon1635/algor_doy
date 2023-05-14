import sys
input = sys.stdin.readline

n, m = map(int, input().split())
weapon = [list(map(int, input().split())) for _ in range(n)]
dp = [[sys.maxsize] * m for _ in range(n)] # [i][j] : i회차, j번 무기
dp[0] = weapon[0]

for stage in range(1, n):
    for cur_w in range(m):
        for ex_w in range(m):
            if cur_w == ex_w: continue
            dp[stage][cur_w] = min(dp[stage][cur_w],
                                   dp[stage - 1][ex_w] + weapon[stage][cur_w])

#for each in dp: print(each)
print(min(dp[-1]))