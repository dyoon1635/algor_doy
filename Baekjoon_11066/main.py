import sys, copy
input = sys.stdin.readline

def dp():
    dp = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): dp[i][i] = 0

    for l in range(2, n + 1): #길이 1 ~ N
        for s in range(1, n + 1): #시작점
            e = s + l - 1
            if e > n: break
            for k in range(s, e):
                dp[s][e] = min(dp[s][e],
                               dp[s][k] + dp[k + 1][e] + partial_sum(s, e))
    return dp[1][-1]

def partial_sum(s, e):
    return cost_sum[e] - cost_sum[s - 1]

T = int(input())
for _ in range(T):
    n = int(input())
    cost = [0] + list(map(int, input().split()))
    cost_sum = copy.deepcopy(cost)
    for i in range(1, n + 1): cost_sum[i] += cost_sum[i - 1]
    print(dp())